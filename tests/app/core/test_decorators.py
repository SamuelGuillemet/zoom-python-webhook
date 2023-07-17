# pylint: disable=unused-argument
from unittest.mock import Mock

import pytest

from app.core.base_webhook_event_schema import BaseWebhookEvent
from app.core.decorators import webhook_handler

webhook_event_test = BaseWebhookEvent(
    payload={"plainToken": "q9ibPhGeRZ6ayx5WTrXjRw"},
    event_ts=1689061099652,
    event="event.test.1",
)


@pytest.mark.asyncio
async def test_webhook_handler():
    mock_handler = Mock()

    @webhook_handler(
        event_name="event.test.1",
        handler_function=mock_handler,
    )
    async def test_func(webhook_event: BaseWebhookEvent):
        assert False  # This should not be called.

    await test_func(webhook_event_test)

    assert mock_handler.called
    assert mock_handler.call_args[0][0]["payload"] == webhook_event_test.payload
    assert mock_handler.call_args[0][0]["event_ts"] == webhook_event_test.event_ts
    assert mock_handler.call_args[0][0]["event"] == webhook_event_test.event


@pytest.mark.asyncio
async def test_webhook_handler_not_event():
    mock_handler = Mock()

    @webhook_handler(
        event_name="wrong",
        handler_function=mock_handler,
    )
    async def test_func(webhook_event: BaseWebhookEvent) -> BaseWebhookEvent:
        return webhook_event

    result = await test_func(webhook_event_test)

    assert result == webhook_event_test
    assert not mock_handler.called


@pytest.mark.asyncio
async def test_webhook_handler_multiple_events_0():
    mock_handler_1 = Mock()
    mock_handler_2 = Mock()

    @webhook_handler(
        event_name="event.test.1",
        handler_function=mock_handler_1,
    )
    @webhook_handler(
        event_name="event.test.2",
        handler_function=mock_handler_2,
    )
    async def test_func(webhook_event: BaseWebhookEvent):
        assert False

    await test_func(webhook_event_test)

    assert mock_handler_1.called
    assert not mock_handler_2.called


@pytest.mark.asyncio
async def test_webhook_handler_multiple_events_1():
    mock_handler_1 = Mock()
    mock_handler_2 = Mock()

    @webhook_handler(
        event_name="event.test.2",
        handler_function=mock_handler_2,
    )
    @webhook_handler(
        event_name="event.test.1",
        handler_function=mock_handler_1,
    )
    async def test_func(webhook_event: BaseWebhookEvent):
        assert False

    await test_func(webhook_event_test)

    assert mock_handler_1.called
    assert not mock_handler_2.called
