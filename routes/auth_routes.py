"""
auth_routes.py
Authentication routes for the API
"""
# Import dependencies
from os import getenv
from requests import post
from fastapi import APIRouter
from firebase_admin import auth
from models import NewUser, LoginUser
from firebase_admin._auth_utils import EmailAlreadyExistsError, PhoneNumberAlreadyExistsError

# Vars
auth_router = APIRouter(prefix="/auth", tags=["Authenticator"])


# Create new user
@auth_router.post("/new")
def create_new_user(new_user: NewUser):
    try:
        # Create new user
        user = auth.create_user(
            display_name=new_user.name,
            email=new_user.email,
            email_verified=new_user.email_verified,
            phone_number=new_user.phone_number,
            password=new_user.password,
            disabled=new_user.disabled
        )
        user_uid = user.uid
        # Set custom claims
        payload = {
            "developer": new_user.developer,
            "employee": new_user.employee
        }
        auth.set_custom_user_claims(user_uid, payload)
        return {"created new user", user_uid}

    # Handle error on connection failure
    except (EmailAlreadyExistsError, PhoneNumberAlreadyExistsError):
        return {"email or phone number already exists"}


# Login user
@auth_router.post("/login")
def login_user(user_details: LoginUser):
    try:
        api_key = getenv("FIREBASE_API_KEY")
        request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
        # Request Firebase API
        payload = {
            "email": user_details.email,
            "password": user_details.password,
            "returnSecureToken": True
        }
        print(payload)
        response = post(url=request_url, params=payload)

        return response.json()

    except Exception as request_error:
        return request_error


# Send password reset link
@auth_router.post("/reset_password")
def send_password_link(user_details: LoginUser):
    try:
        reset_link = auth.generate_password_reset_link(user_details.email)
        return reset_link

    except Exception as error:
        return error


# Delete user
@auth_router.delete("/remove/{uid}")
def delete_user(uid: str):
    try:
        auth.delete_user(uid)
        return {"user delete successfully"}

    except Exception as delete_error:
        return delete_error
