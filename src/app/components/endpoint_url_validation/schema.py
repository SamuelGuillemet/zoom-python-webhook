from pydantic import BaseModel, Field

from app.core.base_webhook_event_schema import (
    BaseResponseWebhookEvent,
    BaseWebhookEvent,
)


class Payload(BaseModel):
    plainToken: str = Field(..., description="The string to hash.")


class UrlValidationWebHook(BaseWebhookEvent):
    """This is the schema for the request body of the webhook for the url_validation event.

    Args:
        WebhookEvent (WebhookEvent): The base webhook model for the schema.
    """

    payload: Payload = Field(
        ...,
        description="Contains a property with the plainToken value, the string to hash.",
    )


class ResponseWebhookUrlValidation(BaseResponseWebhookEvent):
    """This is the schema for the response for endpoint.url_validation webhook.

    Args:
        BaseResponseWebhookEvent (BaseResponseWebhookEvent): The base model for the schema.
    """

    plainToken: str = Field(..., description="The string which has been hashed.")
    encryptedToken: str = Field(..., description="The string hashed.")
