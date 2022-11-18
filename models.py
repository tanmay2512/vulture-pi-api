"""
models.py
Data structure for API
"""
# Import dependencies
from enum import Enum
from pydantic import BaseModel


# New user model
class NewUser(BaseModel):
    name: str
    email: str
    email_verified: bool = False
    phone_number: str
    password: str
    disabled: bool = False
    developer: bool = False
    employee: bool = False

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com",
                "email_verified": False,
                "phone_number": "+91 9319376830",
                "password": "John1234",
                "disabled": False,
                "developer": False,
                "employee": False,
            }
        }


# Login user model
class LoginUser(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "johndoe@gmail.com",
                "password": "John1234"
            }
        }


# Device types
class DeviceType(str, Enum):
    vulture_sky: str = "Vulture Sky"  # Temperature and Humidity
    vulture_moist: str = "Vulture Moist"  # Soil moisture
    vulture_eye: str = "Vulture Eye"  # Motion detector


# New device model
class NewDevice(BaseModel):
    device_type: DeviceType
