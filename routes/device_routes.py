"""
device_routes.py
Manages new device, device registration
NOTE: Some endpoints are only for authenticated employees
"""
# Import dependencies
from models import NewDevice
from fastapi import APIRouter
from systems.database import device_collection
from systems.utils import generate_device_serial_number, current_datetime, validate_device

# Device router
device_router = APIRouter(prefix="/devices", tags=["Devices"])


# Create new device
@device_router.post("/create")
def create_new_device(device_details: NewDevice):
    device_serial_number = generate_device_serial_number(device_details.device_type)
    device_check = validate_device(device_serial_number, device_details.device_type)

    # Proceed to create new device
    if device_check == 1:
        device_payload = {
            "device serial number": device_serial_number,
            "device type": device_details.device_type,
            "created on": str(current_datetime())
        }

        device_collection.insert_one(device_payload)
        return {"msg": "device created successfully", "device serial number": device_serial_number}

    # Reject new device creation
    if device_check == 0:
        return {"serial number already in use try again until success"}
