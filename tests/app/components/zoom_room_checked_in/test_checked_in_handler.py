import pytest
from pydantic import ValidationError

from app.components.zoom_room_checked_in import handler_function

body = {
    "event": "zoomroom.checked_in",
    "event_ts": 1626230691572,
    "payload": {
        "account_id": "AAAAAABBBB",
        "object": {
            "id": "abcD3ojfdbjfg",
            "room_name": "My Zoom Room",
            "calendar_name": "mycalendar@example.com",
            "email": "jchill@example.com",
            "event_id": "AbbbbbGYxLTc3OTVkMzFmZDc0MwBGAAAAAAD48FI58voYSqDgJePOSZ",
            "change_key": "DwAAABYAAABQ/N0JvB/FRqv5UT2rFfkVAAE2XqVw",
            "resource_email": "zroom1@example.com",
            "calendar_id": "mycalendar@example.com",
            "calendar_type": "2",
            "api_type": "0",
        },
    },
}


def test_checked_in_handler():
    assert handler_function(body).model_dump() == {"message": "Checked in!"}


def test_checked_in_handler_invalid_payload():
    body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(body)
