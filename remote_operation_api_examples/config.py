import dataclasses
from urllib.parse import urljoin
from uuid import UUID

from requests import Session, post


def create_session(base_url, username, password):
    session = Session()
    response_login = post(
        urljoin(base_url, "/auth/access-token"),
        {"username": username, "password": password},
    )
    response_login.raise_for_status()

    session.headers.update(
        {"Authorization": f"Bearer {response_login.json()['access_token']}"},
    )

    return session


@dataclasses.dataclass
class Config:
    username: str
    password: str
    platform_url: str
    user_id: UUID  # todo remove once the endpoint to retrieve the user_id is available
    _session = None

    @property
    def session(self):
        if self._session:
            return self._session
        self._session = create_session(self.platform_url, self.username, self.password)
        return self._session
