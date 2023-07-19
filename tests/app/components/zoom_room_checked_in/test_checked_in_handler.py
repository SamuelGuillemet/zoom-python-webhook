import pytest
from pydantic import ValidationError

from app.components.zoom_room_checked_in import handler_function


def test_checked_in_handler(checked_in_body):
    assert handler_function(checked_in_body).model_dump() == {"message": "Checked in!"}


def test_checked_in_handler_invalid_payload(checked_in_body):
    checked_in_body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(checked_in_body)
