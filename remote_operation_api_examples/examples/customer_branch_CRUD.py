from json import dumps
from urllib.parse import urljoin

from config import Config


def create_and_delete_customer_branch(config: Config):
    """
    This example shows how to handle basic CRUD operations using the entity Customer Branch as an example.
    It creates one instance of a customer branch providing fake values, checks that the creation is successful,
    performs a GET on the same entity again to demonstrate the GET endpoint and then deletes it afterwards.
    """
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
    branch_id = response.json()["id"]
    print(f"Customer Branch successfully created with id {branch_id}")

    response = session.get(url=urljoin(config.platform_url, f"/branches/{branch_id}"))
    print(f"Customer Branch successfully retrieved:\n{dumps(response.json(),indent=4)}\n")

    response = session.delete(url=urljoin(config.platform_url, f"/branches/{branch_id}"))
    response.raise_for_status()
    print("Customer Branch successfully deleted")
