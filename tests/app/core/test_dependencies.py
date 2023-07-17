from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import HTTPException, Request

from app.core.base_webhook_event_schema import BaseWebhookEvent
from app.core.dependencies import verify_webhook_signature

body_test = BaseWebhookEvent(
    payload={"plainToken": "q9ibPhGeRZ6ayx5WTrXjRw"},
    event_ts=1689061099652,
    event="endpoint.url_validation",
)

headers_test = {
    "x-zm-request-timestamp": "1689061099",
    "x-zm-signature": "v0=018da294385a446c50fce872fe2a2bb6273ac701bf59f3305c819de787291e1c",
}


async def mocked_request(json_data):
    request = MagicMock(spec=Request)
    request.json = AsyncMock(return_value=json_data)
    return request


@pytest.mark.asyncio
async def test_verify_webhook_signature():
    # Prepare the mock request
    mock_request = await mocked_request(json_data=body_test.model_dump())

    # Call the function with the mock request
    response = await verify_webhook_signature(
        request=mock_request,
        x_zm_signature=headers_test["x-zm-signature"],
        x_zm_request_timestamp=headers_test["x-zm-request-timestamp"],
    )

    # Assert the response
    assert response is None


@pytest.mark.asyncio
async def test_verify_webhook_signature_invalid():
    # Prepare the mock request
    mock_request = await mocked_request(json_data=body_test.model_dump())

    # Call the function with the mock request
    with pytest.raises(HTTPException) as exc_info:
        await verify_webhook_signature(
            request=mock_request,
            x_zm_signature="wrong",
            x_zm_request_timestamp=headers_test["x-zm-request-timestamp"],
        )

    # Assert the response
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "Invalid signature."
