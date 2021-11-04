from urllib.parse import urljoin

from config import Config
from utils import create_customer_branch


def create_order(config: Config):
    """
    This example shows how to create an order

    """
    branch_id = create_customer_branch(config)
    request_body = {
        "order_pickup_branch_id": branch_id,
        "order_delivery_address": "Hello",
        "order_delivery_location": {"latitude": 52.520008, "longitude": 13.404954},
    }

    response = config.session.post(url=urljoin(config.platform_url, "orders/"), json=request_body)
    response.raise_for_status()
    print("Order successfully created")
    return response.json()["id"]
