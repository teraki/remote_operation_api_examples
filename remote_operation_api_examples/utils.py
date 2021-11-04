from urllib.parse import urljoin

from config import Config


def create_customer_branch(config: Config):
    session = config.session
    response = session.post(
        url=urljoin(config.platform_url, "/branches"),
        json={
            "branch_name": "test_branch",
            "branch_address": "Somewhere",
            "branch_location": {"latitude": 52.520008, "longitude": 13.404954},
            "customer_id": str(config.user_id),
        },
    )

    response.raise_for_status()
    return response.json()["id"]
