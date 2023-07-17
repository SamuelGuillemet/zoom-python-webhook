from fastapi import APIRouter

from app.api.v1.api import api_v1_router
from app.api.v1.endpoints.webhook import router


def test_api_v1_router():
    assert isinstance(api_v1_router, APIRouter)


def test_api_v1_router_include_webhook_router():
    for route in router.routes:
        assert route in api_v1_router.routes
