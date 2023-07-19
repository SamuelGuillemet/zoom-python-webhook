import pytest


@pytest.fixture
def url_validation_body():
    return {
        "payload": {"plainToken": "q9ibPhGeRZ6ayx5WTrXjRw"},
        "event_ts": 1689061099652,
        "event": "endpoint.url_validation",
    }


@pytest.fixture
def checked_in_body():
    return {
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


@pytest.fixture
def checked_out_body():
    return {
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


@pytest.fixture
def sensor_data_body():
    return {
        "event": "zoomroom.sensor_data",
        "event_ts": 1626230691572,
        "payload": {
            "account_id": "AAAAAABBBB",
            "object": {
                "id": "abcD3ojfdbjfg",
                "room_name": "My Zoom Room",
                "device_id": "NiVvY1NWpE2nulNrhVjgU4jD0swziVrXBbaFZyC3u+o=",
                "sensor_data": [
                    {
                        "date_time": "2022-06-19T00:00:00Z",
                        "sensor_type": "REAL_TIME_PEOPLE_COUNT",
                        "sensor_value": "20",
                    }
                ],
            },
        },
    }


@pytest.fixture
def not_supported_event_body():
    return {
        "event": "not_supported_event",
        "event_ts": 1626230691572,
        "payload": {},
    }
