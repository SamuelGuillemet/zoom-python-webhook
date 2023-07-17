""" API v1 router. """

import importlib

from fastapi import APIRouter

from app.api.v1 import endpoints

endpoints_module = [
    importlib.import_module(f"app.api.v1.endpoints.{module}")
    for module in endpoints.__all__
]

api_v1_router = APIRouter()

for module in endpoints_module:
    api_v1_router.include_router(module.router)
