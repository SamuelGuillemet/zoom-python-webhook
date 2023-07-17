""" Webhook endpoint. """

import logging
from typing import Union

from fastapi import APIRouter, Depends, HTTPException

from app.components import (
    endpoint_url_validation,
    zoom_room_checked_in,
    zoom_room_checked_out,
)
from app.core.base_webhook_event_schema import BaseWebhookEvent, ErrorModel
from app.core.decorators import webhook_handler
from app.core.dependencies import verify_webhook_signature

logger = logging.getLogger("app.api.v1.webhook")

router = APIRouter(tags=["webhook"], prefix="/webhook")

# Common responses for the error cases.
responses = {
    403: {"description": "Webhook signature verification failed.", "model": ErrorModel},
    501: {"description": "Webhook event not supported.", "model": ErrorModel},
}

# Union of all response models for the webhook handlers.
ResponseModel = Union[
    endpoint_url_validation.response_model,
    zoom_room_checked_in.response_model,
    zoom_room_checked_out.response_model,
]


@router.post(
    "",  # Will be /webhook
    dependencies=[Depends(verify_webhook_signature)],
    response_model=ResponseModel,
    responses={**responses},
)
@webhook_handler(
    event_name=endpoint_url_validation.event_name,
    handler_function=endpoint_url_validation.handler_function,
)
@webhook_handler(
    event_name=zoom_room_checked_in.event_name,
    handler_function=zoom_room_checked_in.handler_function,
)
@webhook_handler(
    event_name=zoom_room_checked_out.event_name,
    handler_function=zoom_room_checked_out.handler_function,
)
async def webhook_route(webhook_event: BaseWebhookEvent):
    """
    Handle incoming webhook events.

    Args:
        webhook_event (BaseWebhookEvent): The incoming webhook event.

    Raises:
        HTTPException: If the webhook event is not supported.
    """
    logger.warning("Unhandled webhook event: %s", webhook_event.event)
    raise HTTPException(
        detail=f"Webhook event {webhook_event.event} not supported.",
        status_code=501,
    )
