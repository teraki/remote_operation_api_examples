from urllib.parse import urljoin

from remote_operation_api_examples.config import Config


def list_vehicles(config: Config):
    """This examples shows how to list the vehicles"""
    response = config.session.get(url=urljoin(config.platform_url, "vehicles/"))
    response.raise_for_status()
    print(f"Vehicles successfully retrieved\n {response.json()}")


def get_vehicle(config: Config):
    """This examples shows how to retrieve a vehicle's information and inspect the status"""
    vehicle_id = "608b17eb-78b8-45e5-835f-053e7ba93e72"
    response = config.session.get(url=urljoin(config.platform_url, f"vehicles/{vehicle_id}"))
    response.raise_for_status()
    print("Vehicle successfully retrieved.")
    print(f"Status: {response.json()['vehicle_status']}")
