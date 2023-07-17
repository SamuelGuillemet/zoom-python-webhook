""" This module contains decorators for the webhook handlers. """

from typing import Awaitable, Callable

from app.core.base_webhook_event_schema import (
    BaseResponseWebhookEvent,
    BaseWebhookEvent,
)


def webhook_handler(
    event_name: str, handler_function: Callable[[dict], BaseResponseWebhookEvent]
) -> Callable:
    """This function is a decorator that registers a webhook handler.

    Args:
        event_name (str): The name of the webhook event.
        handler_function (Callable): The handler function for the webhook event.

    Returns:
        Callable: The decorator will call either the handler function for the webhook event,
        or the base function if the event name does not match.
    """

    def decorator(func: Callable[..., Awaitable]) -> Callable:
        async def wrapper(webhook_event: BaseWebhookEvent):
            if webhook_event.event != event_name:
                return await func(webhook_event)

            return handler_function(webhook_event.model_dump())

        return wrapper

    return decorator
