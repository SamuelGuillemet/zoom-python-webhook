import logging

from .schema import CheckedInWebHook, ResponseWebhookCheckedIn

logger = logging.getLogger("app.components.zoomroom.checked_in")


def checked_in_handler(body: dict):
    check_in = CheckedInWebHook(**body)

    logger.debug(
        "New checked_in event in room %s [%s] associated to %s, for event %s.",
        check_in.payload.object.room_name,
        check_in.payload.object.id,
        check_in.payload.object.resource_email,
        check_in.payload.object.event_id,
    )
    # For the checked-in event I would at least:
    #   event | event_ts | account_id | ZRid | room_name | email | event_id | change_key | api_type
    logger.info(
        "%s | %s | %s | %s | %s | %s | %s | %s | %s",
        check_in.event,
        check_in.event_ts,
        check_in.payload.account_id,
        check_in.payload.object.id,
        check_in.payload.object.room_name,
        check_in.payload.object.email,
        check_in.payload.object.event_id,
        check_in.payload.object.change_key,
        check_in.payload.object.api_type,
    )

    # TODO: Add code here to handle the checked_in event.

    return ResponseWebhookCheckedIn(
        message="Checked in!",
    )
