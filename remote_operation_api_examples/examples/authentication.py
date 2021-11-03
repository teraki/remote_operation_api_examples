from urllib.parse import urljoin

from config import Config
from requests import Session, post


def authenticate(config:Config):
    session = Session()
    response_login = post(
        urljoin(config.platform_url,"/auth/access-token"),
        {"username": config.username, "password": config.password},
    )
    response_login.raise_for_status()

    token=response_login.json()['access_token']
    session.headers.update(
        {"Authorization": f"Bearer {token}"},
    )
    print("Authentication successful")