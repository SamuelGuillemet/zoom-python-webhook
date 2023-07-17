from fastapi.testclient import TestClient

from app.core.dependencies import verify_webhook_signature
from app.main import app

client = TestClient(app)


async def override_verify_webhook_signature():
    pass


url_validation_body = {
    "payload": {"plainToken": "q9ibPhGeRZ6ayx5WTrXjRw"},
    "event_ts": 1689061099652,
    "event": "endpoint.url_validation",
}

checked_in_body = {
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

checked_out_body = {
    "event": "zoomroom.checked_out",
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

not_supported_event_body = {
    "event": "not_supported_event",
    "event_ts": 1626230691572,
    "payload": {},
}


def test_url_validation():
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=url_validation_body,
    )

    assert response.status_code == 200


def test_check_in():
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=checked_in_body,
    )

    assert response.status_code == 200


def test_check_out():
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=checked_out_body,
    )

    assert response.status_code == 200


def test_not_supported_event():
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=not_supported_event_body,
    )

    assert response.status_code == 501
