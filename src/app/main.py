"""Main module for the application."""

import tomllib

from fastapi import FastAPI

from app.api.v1.api import api_v1_router
from app.core.config import settings
from app.utils.logger import setup_logs

with open("pyproject.toml", "rb") as f:
    version = tomllib.load(f)["tool"]["poetry"]["version"]

app = FastAPI(
    title="Zoom webhook",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    version=version,
)

app.include_router(api_v1_router, prefix=settings.API_V1_PREFIX)

setup_logs("app")
