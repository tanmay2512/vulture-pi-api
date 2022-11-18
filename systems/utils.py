"""
utils.py
Utility functions
"""
# Import dependencies
from random import randint
from datetime import datetime
from firebase_admin.storage import bucket
from systems.database import get_app_data
from systems.database import get_device_data
from firebase_admin.auth import verify_id_token
from firebase_admin.exceptions import UnknownError
from firebase_admin import initialize_app, credentials


# Configure firebase
def config_firebase():
    try:
        # Credentials file located in "config" dir
        creds = credentials.Certificate("config/Firebase config.json")
        app = initialize_app(creds, {
            "databaseURL": "https://vulture-web-default-rtdb.firebaseio.com",
            "storageBucket": "vulture-web.appspot.com"
        })
        print("Firebase configured.......")
        return app

    # Handle error on connection failure
    except UnknownError as conn_error:
        raise conn_error

    # Return final message to client
    finally:
        return "email or phone number already exists."


# Generate unique device id
def generate_device_serial_number(device_type: str):
    device_identifiers = ["VS", "VM", "VE"]
    unique_num = randint(1000, 9999)

    # Check device type
    if device_type == "Vulture Sky":
        serial_number = f"{device_identifiers[0]}-{unique_num}"
        return serial_number

    elif device_type == "Vulture Moist":
        serial_number = f"{device_identifiers[1]}-{unique_num}"
        return serial_number

    elif device_type == "Vulture Eye":
        serial_number = f"{device_identifiers[2]}-{unique_num}"
        return serial_number


# Current date and time
def current_datetime():
    current_date = datetime.now()
    return current_date


# Validate device
def validate_device(device_serial_number: str):
    device_status = get_device_data(device_serial_number, "device type")
    if device_status is None:  # Device not exist. Safe to create new device
        return 1

    elif device_status is None:  # Device exist. Cancel the operation
        return 0


# Validate app
def validate_app(app_name: str, status: bool):
    if not status:
        return 0

    elif status:
        app_check = get_app_data(app_name)
        if app_check is None:
            return 1

        elif app_check is not None:
            return 0


# Verify id token of user
def verify_id_token_user(id_token: str):
    decoded_token = verify_id_token(id_token)
    return decoded_token


# Storage bucket
def upload_file(filepath: str):
    buckets = bucket()
    blob = buckets.blob(filepath)
    blob.upload_from_filename(filepath)
    blob.make_public()
