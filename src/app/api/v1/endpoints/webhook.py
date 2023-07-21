""" Webhook endpoint. """

import logging
from typing import Callable, Union

from fastapi import APIRouter, Depends, HTTPException

from app import components
from app.core.base_webhook_event_schema import (
    BaseResponseWebhookEvent,
    BaseWebhookEvent,
    ErrorModel,
)
from app.core.dependencies import verify_webhook_signature
from app.utils.load_submodules import load_submodules

logger = logging.getLogger("app.api.v1.webhook")

router = APIRouter(tags=["webhook"], prefix="/webhook")

# Load all webhook components and create a list of tuples containing
# the event name, handler function, and response model.
components_tuple: list[
    tuple[str, Callable[..., BaseResponseWebhookEvent], BaseResponseWebhookEvent]
] = [
    (
        getattr(component, "event_name"),
        getattr(component, "handler_function"),
        getattr(component, "response_model"),
    )
    for component in load_submodules(components)
]


@router.post(
    "",  # Will be /webhook
    dependencies=[Depends(verify_webhook_signature)],
    response_model=Union[
        tuple(response_model for _, _, response_model in components_tuple)  # type: ignore
    ],
    responses={
        403: {
            "description": "Webhook signature verification failed.",
            "model": ErrorModel,
        },
        501: {"description": "Webhook event not supported.", "model": ErrorModel},
    },
)
async def webhook_route(webhook_event: BaseWebhookEvent):
    """
    Handle incoming webhook events.

    Args:
        webhook_event (BaseWebhookEvent): The incoming webhook event.

    Raises:
        HTTPException: If the webhook event is not supported.
    """
    for event_name, handler_function, _ in components_tuple:
        if webhook_event.event == event_name:
            return handler_function(webhook_event.model_dump())

    logger.warning("Unhandled webhook event: %s", webhook_event.event)
    raise HTTPException(
        detail=f"Webhook event {webhook_event.event} not supported.",
        status_code=501,
    )
