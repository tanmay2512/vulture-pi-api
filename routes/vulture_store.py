"""
vulture_store.py
Online repository of apps for Vulture Pi
NOTE: APPS CAN ONLY BE UPLOADED BY DEVELOPERS
"""
import time
# Import dependencies
from json import loads
from fastapi import APIRouter
from fastapi import UploadFile, File
from systems.database import apps_collection
from systems.utils import verify_id_token_user, upload_file, validate_app

# Repository router
repo_router = APIRouter(prefix="/vstore", tags=["Vulture Store"])


# Upload new app
@repo_router.post("/upload_new")
def upload_new_app(id_token: str, files: UploadFile = File(...)):
    report_content = files.file.read()
    report_json = loads(report_content)
    dev_check = verify_id_token_user(id_token)
    app_name = report_json['details']['app name']
    if dev_check:
        app_check = validate_app(app_name)
        if app_check:
            deb_filename = report_json["report"]["deb package filename"]
            repo_url = upload_file(deb_filename)
            db_payload = {
                "app name": report_json['details']["app name"],
                "repo url": repo_url,
                "developer": report_json['details']['developed by'],
                "file size": report_json['report']['file size'],
                "support website": report_json['support']['website'],
                "support email": report_json['support']['support email']
            }
            apps_collection.insert_one(db_payload)

        elif not app_check:
            return {"app name already in use"}

        return {"app published successfully"}

    elif not dev_check:
        return {"please create a developer account"}
