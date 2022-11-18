"""
database.py
Requests data from MongoDB stored in different collections.
"""
# Import dependencies
from os import getenv
from pymongo.mongo_client import MongoClient


# Connect to db
def connect_db():
    db_name = "Vulture_Web_DB"
    db_url = getenv("DB_URL")
    client = MongoClient(db_url)
    parent_db = client[str(db_name)]
    return parent_db


# Refer to db
db = connect_db()

# Collections
device_collection = db["Devices"]
apps_collection = db["Apps"]


# Get device data
def get_device_data(serial_number: str, key: str):
    device_data = device_collection.find_one({"device serial number": serial_number})
    if device_data is None:
        return None

    elif device_data is not None:
        return device_data[key]


# Get app data
def get_app_data(app_name: str, key: str = "app name"):
    app_data = apps_collection.find_one({"app name": app_name})
    if app_data is None:
        return None

    elif app_data is not None:
        return app_data[key]
