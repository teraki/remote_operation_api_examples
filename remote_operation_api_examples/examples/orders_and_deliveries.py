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


def create_delivery(config: Config):
    """
    This example shows how to create a delivery with two orders
    """

    # we create two orders
    order_id_1 = create_order(config)
    order_id_2 = create_order(config)

    # we update their status to READY_DELIVERY, meaning that they are ready to be included in a delivery and picked up
    request_body = {"order_status": "READY_DELIVERY"}
    response = config.session.post(url=urljoin(config.platform_url, f"orders/{order_id_1}/status"), json=request_body)
    response.raise_for_status()
    response = config.session.post(url=urljoin(config.platform_url, f"orders/{order_id_2}/status"), json=request_body)
    response.raise_for_status()

    # we then create a delivery using a demo driver id and a demo vehicle
    body = {
        "order_ids": [order_id_1, order_id_2],
        "vehicle_id": "608b17eb-78b8-45e5-835f-053e7ba93e72",
        "driver_id": "378169e0-920e-4256-913c-b2536d20ad00",
    }
    response = config.session.post(url=urljoin(config.platform_url, "deliveries"), json=body)
    response.raise_for_status()

    print("Delivery successfully created")
