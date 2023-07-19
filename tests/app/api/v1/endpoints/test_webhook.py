from fastapi.testclient import TestClient

from app.core.dependencies import verify_webhook_signature
from app.main import app

client = TestClient(app)


async def override_verify_webhook_signature():
    pass


def test_url_validation(url_validation_body):
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=url_validation_body,
    )

    assert response.status_code == 200


def test_check_in(checked_in_body):
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=checked_in_body,
    )

    assert response.status_code == 200


def test_check_out(checked_out_body):
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=checked_out_body,
    )

    assert response.status_code == 200


def test_sensor_data(sensor_data_body):
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=sensor_data_body,
    )

    assert response.status_code == 200


def test_not_supported_event(not_supported_event_body):
    app.dependency_overrides[
        verify_webhook_signature
    ] = override_verify_webhook_signature
    response = client.post(
        "api/v1/webhook",
        json=not_supported_event_body,
    )

    assert response.status_code == 501
