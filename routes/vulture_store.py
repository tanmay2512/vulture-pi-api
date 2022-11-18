"""
vulture_store.py
Online repository of apps for Vulture Pi
NOTE: APPS CAN ONLY BE UPLOADED BY DEVELOPERS
"""
import time
# Import dependencies
from os import getcwd
from os import system
from json import loads
from fastapi import APIRouter
from fastapi import UploadFile, File
from systems.utils import verify_id_token_user, upload_file

# Repository router
repo_router = APIRouter(prefix="/vstore", tags=["Vulture Store"])


# Upload new app
@repo_router.post("/upload_new")
def upload_new_app(id_token: str, files: UploadFile = File(...)):
    report_content = files.file.read()
    report_json = loads(report_content)
    security_status = report_json["details"]["safe"]

    # If safe
    if security_status:
        token = verify_id_token_user(id_token)
        dev_check = token['developer']
        if dev_check:
            deb_filepath = report_json["report"]["deb package filepath"]
            deb_filename = report_json["report"]["deb package filename"]
            try:
                system(f"copy {deb_filepath} {getcwd()}")
                upload_file(deb_filename)
                return {"file uploaded"}

            except FileNotFoundError as file_not_found:
                return file_not_found

        elif not dev_check:
            return {"Denied"}

    # If not safe
    if not security_status:
        return {f"{files.filename} cannot be uploaded due to security reasons, please visit google.com for help"}
