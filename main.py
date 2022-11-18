"""
main.py
Root configuration of the api
"""
# Import dependencies
from os import getenv
from uvicorn import run
from pathlib import Path
from fastapi import FastAPI
from dotenv import load_dotenv
from systems.database import connect_db
from systems.utils import config_firebase
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routes.auth_routes import auth_router
from routes.vulture_store import repo_router
from routes.device_routes import device_router

# FastAPI app
app = FastAPI()
db_url = getenv("DB_URL")

# Middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers
app.include_router(auth_router)
app.include_router(device_router)
app.include_router(repo_router)


# Configure systems on startup
@app.on_event("startup")
def on_startup():
    # Configure firebase and connect to MongoDB
    config_firebase()
    load_dotenv(Path("config/settings.env"))
    connect_db()


if __name__ == "__main__":
    run("main:app", port=8000, log_level="info")
