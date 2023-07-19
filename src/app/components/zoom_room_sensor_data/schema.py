from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field

from app.core.base_webhook_event_schema import (
    BaseResponseWebhookEvent,
    BaseWebhookEvent,
)


class SensorType(Enum):
    CO2 = "CO2"
    TEMPERATURE = "TEMPERATURE"
    REAL_TIME_PEOPLE_COUNT = "REAL_TIME_PEOPLE_COUNT"
    HUMIDITY = "HUMIDITY"
    VOC = "VOC"


class SensorData(BaseModel):
    date_time: datetime = Field(
        ..., description="The time when the sensor data was reported."
    )
    sensor_type: SensorType = Field(..., description="The type of sensor.")
    sensor_value: str = Field(..., description="The value of the sensor.")


class Object(BaseModel):
    id: str = Field(..., description="The ID of the Zoom Room.")
    room_name: str = Field(..., description="The name of the Zoom Room.")
    device_id: str = Field(..., description="The ID of the device.")
    sensor_data: List[SensorData] = Field(
        ..., description="The sensor data reported by the device."
    )


class Payload(BaseModel):
    account_id: str = Field(..., description="The account ID of the Zoom account.")
    object: Object = Field(..., description="Information about the Zoom Room.")


class SensorDataWebHook(BaseWebhookEvent):
    """This is the schema for the request body of the webhook for the zoomroom.sensor_data event.

    Args:
        WebhookEvent (WebhookEvent): The base webhook model for the schema.
    """

    payload: Payload = Field(
        ...,
        description="Contains all the information about the Zoom Room that reported the sensor data.",
    )


class ResponseWebhookSensorData(BaseResponseWebhookEvent):
    """This is the schema for the response for zoomroom.sensor_data webhook.

    Args:
        BaseResponseWebhookEvent (BaseResponseWebhookEvent): The base model for the schema.
    """

    message: str = Field(..., description="The message of the response.")
