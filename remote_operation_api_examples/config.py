import dataclasses
from typing import Optional
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


def get_user_id(session: Session, platform_url) -> UUID:
    response_me = session.post(
        urljoin(platform_url, "/auth/me"),
    )
    response_me.raise_for_status()
    return response_me.json()["id"]


@dataclasses.dataclass
class Config:
    username: str
    password: str
    platform_url: str
    _user_id: UUID = None
    _session: Optional[Session] = None

    @property
    def session(self):
        if self._session:
            return self._session
        self._session = create_session(self.platform_url, self.username, self.password)
        return self._session

    @property
    def user_id(self):
        if self._user_id:
            return self._user_id
        self._user_id = get_user_id(self.session, platform_url=self.platform_url)
        return self._user_id
