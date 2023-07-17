import pytest
from pydantic import ValidationError

from app.components.endpoint_url_validation import handler_function

body = {
    "payload": {"plainToken": "plain_token"},
    "event_ts": 1689061099652,
    "event": "endpoint.url_validation",
}


def test_url_validation_handler():
    assert handler_function(body).model_dump() == {
        "plainToken": "plain_token",
        "encryptedToken": "6444317b153180cf15822bec8a313bda9c41e3b6a5f009785e8b833ff65010fc",
    }


def test_url_validation_handler_invalid_payload():
    body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(body)
