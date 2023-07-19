from typing import Optional

from pydantic import BaseModel, Field

from app.core.base_webhook_event_schema import (
    BaseResponseWebhookEvent,
    BaseWebhookEvent,
)


class Object(BaseModel):
    id: str = Field(..., description="The ID of the Zoom Room.")
    room_name: str = Field(..., description="The name of the Zoom Room.")
    calendar_name: str = Field(..., description="The name of the calendar.")
    email: str = Field(..., description="The Zoom Room's associated email address.")
    event_id: str = Field(..., description="The ID of the event.")
    change_key: str = Field(
        ...,
        description="The change key of the event, only for Microsoft Exchange calendar.",
    )
    resource_email: str = Field(..., description="The email address of the calendar.")
    calendar_id: str = Field(..., description="The ID of the calendar.")
    calendar_type: str = Field(..., description="The type of the calendar.")
    api_type: Optional[str] = Field(..., description="The type of the API.")


class Payload(BaseModel):
    account_id: str = Field(..., description="The account ID of the Zoom account.")
    object: Object = Field(..., description="Information about the Zoom Room.")


class CheckedOutWebHook(BaseWebhookEvent):
    """This is the schema for the request body of the webhook for the zoomroom.checked_out event.

    Args:
        WebhookEvent (WebhookEvent): The base webhook model for the schema.
    """

    payload: Payload = Field(
        ...,
        description="Contains all the information about the Zoom Room that checked out.",
    )


class ResponseWebhookCheckedOut(BaseResponseWebhookEvent):
    """This is the schema for the response for zoomroom.checked_out webhook.

    Args:
        BaseResponseWebhookEvent (BaseResponseWebhookEvent): The base model for the schema.
    """

    message: str = Field(..., description="The message of the response.")
