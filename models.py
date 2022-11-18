<<<<<<< HEAD
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


# App details
class NewApp(BaseModel):
    app_name: str
    developer: str
    datetime_published: str
    file_size: int
    support_website: str
    support_email: str

    class Config:
        schema_extra = {
            "example": {
                "app_name": "Workflow Automation",
                "developer": "John Doe",
                "datetime published": "Today",
                "file_size": 15,
                "support_website": "www.google.com",
                "support_email": "hello@gmail.com"
            }
        }
=======
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


# App details
class NewApp(BaseModel):
    app_name: str
    developer: str
    datetime_published: str
    file_size: int
    support_website: str
    support_email: str

    class Config:
        schema_extra = {
            "example": {
                "app_name": "Workflow Automation",
                "developer": "John Doe",
                "datetime published": "Today",
                "file_size": 15,
                "support_website": "www.google.com",
                "support_email": "hello@gmail.com"
            }
        }
>>>>>>> a40921b4781463f209857e35f9adcfd837afa9f1
