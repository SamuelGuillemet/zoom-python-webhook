import pytest
from pydantic import ValidationError

from app.components.endpoint_url_validation import handler_function


def test_url_validation_handler(url_validation_body):
    assert handler_function(url_validation_body).model_dump() == {
        "plainToken": "q9ibPhGeRZ6ayx5WTrXjRw",
        "encryptedToken": "7172d1f047a422bd6e327228425bc62c46677352a96c34324be07301ca45a319",
    }


def test_url_validation_handler_invalid_payload(url_validation_body):
    url_validation_body["payload"] = {}

    with pytest.raises(ValidationError):
        handler_function(url_validation_body)
