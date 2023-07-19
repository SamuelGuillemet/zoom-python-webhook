import pytest
from pydantic import ValidationError

from app.components.zoom_room_checked_out import handler_function


def test_checked_out_handler(checked_out_body):
    assert handler_function(checked_out_body).model_dump() == {
        "message": "Checked out!"
    }


def test_checked_out_handler_invalid_payload(checked_out_body):
    checked_out_body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(checked_out_body)
