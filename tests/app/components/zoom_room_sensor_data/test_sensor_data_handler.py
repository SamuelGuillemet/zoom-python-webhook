import pytest
from pydantic import ValidationError

from app.components.zoom_room_sensor_data import handler_function


def test_sensor_data_handler(sensor_data_body):
    assert handler_function(sensor_data_body).model_dump() == {
        "message": "Sensor data event received."
    }


def test_sensor_data_handler_no_data(sensor_data_body):
    sensor_data_body["payload"]["object"]["sensor_data"] = []
    assert handler_function(sensor_data_body).model_dump() == {
        "message": "No sensor data in the payload."
    }


def test_sensor_data_handler_invalid_payload(sensor_data_body):
    sensor_data_body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(sensor_data_body)
