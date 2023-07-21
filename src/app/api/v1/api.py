""" API v1 router. """

from fastapi import APIRouter

from app.api.v1 import endpoints
from app.utils.load_submodules import load_submodules

endpoints_module = load_submodules(endpoints)

api_v1_router = APIRouter()

for module in endpoints_module:
    api_v1_router.include_router(module.router)
