import hashlib
import hmac
import logging

from app.core.config import settings

from .schema import ResponseWebhookUrlValidation, UrlValidationWebHook

logger = logging.getLogger("app.components.endpoint.url_validation")


def url_validation_handler(body: dict):
    url_validation = UrlValidationWebHook(**body)

    logger.info("Handling url_validation event.")

    validate_hash = hmac.new(
        key=bytes(settings.ZOOM_WEBHOOK_SECRET_TOKEN, "utf-8"),
        msg=bytes(url_validation.payload.plainToken, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    return ResponseWebhookUrlValidation(
        plainToken=url_validation.payload.plainToken,
        encryptedToken=validate_hash,
    )
