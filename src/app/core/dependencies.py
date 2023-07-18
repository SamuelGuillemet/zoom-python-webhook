""" FastAPI dependencies. """

import hashlib
import hmac
import json
import logging
from typing import Annotated

from fastapi import Header, HTTPException, Request

from app.core.base_webhook_event_schema import BaseWebhookEvent
from app.core.config import settings

logger = logging.getLogger("app.core.dependencies")


async def verify_webhook_signature(
    request: Request,
    x_zm_signature: Annotated[str, Header()],
    x_zm_request_timestamp: Annotated[str, Header()],
):
    """
    Verify the signature of a Zoom webhook request.

    Args:
        request (Request): The incoming request object.
        x_zm_signature (Annotated[str, Header()]): The signature included in the request headers.
        x_zm_request_timestamp (Annotated[str, Header()]): The timestamp included in the request headers.

    Raises:
        HTTPException: If the signature is invalid.

    """
    body = await request.json()
    # construct the message string
    message = f"v0:{x_zm_request_timestamp}:{json.dumps(body, separators=(',', ':'))}"

    # hash the message string with your Webhook Secret Token and prepend the version semantic
    hash_for_verify = hmac.new(
        key=bytes(settings.ZOOM_WEBHOOK_SECRET_TOKEN, "utf-8"),
        msg=bytes(message, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    signature = f"v0={hash_for_verify}"

    # validate the request came from Zoom
    if x_zm_signature != signature:
        logger.warning("Invalid signature: %s != %s", x_zm_signature, signature)
        raise HTTPException(
            status_code=403,
            detail="Invalid signature.",
        )

    BaseWebhookEvent.model_validate(body)
    logger.debug("Signature verified.")
