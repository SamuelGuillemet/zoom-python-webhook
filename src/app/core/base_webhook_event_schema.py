"""Those are the basic schemas for the webhook events."""

from pydantic import BaseModel, Field


class BaseWebhookEvent(BaseModel):
    """This is the schema for the request body of a basic webhook event.

    Args:
        BaseModel (BaseModel): The base model for the schema.
    """

    event: str = Field(..., description="The type of the webhook event.")
    event_ts: int = Field(..., description="The timestamp of the webhook event.")
    payload: dict = Field(..., description="The payload of the webhook event.")


class BaseResponseWebhookEvent(BaseModel):
    """This is the schema for the response of a webhook call.

    Args:
        BaseModel (BaseModel): The base model for the schema.
    """


class ErrorModel(BaseModel):
    """This is the schema for the response of a webhook call.

    Args:
        BaseModel (BaseModel): The base model for the schema.
    """

    detail: str = Field(..., description="The error message.")
