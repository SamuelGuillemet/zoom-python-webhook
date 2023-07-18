import logging

from .schema import CheckedOutWebHook, ResponseWebhookCheckedOut

logger = logging.getLogger("app.components.zoomroom.checked_out")


def checked_out_handler(body: dict):
    check_out = CheckedOutWebHook(**body)

    logger.debug(
        "New checked_out event in room %s [%s] associated to %s, for event %s.",
        check_out.payload.object.room_name,
        check_out.payload.object.id,
        check_out.payload.object.resource_email,
        check_out.payload.object.event_id,
    )

    # For the checked-out event I would at least:
    #   event | event_ts | account_id | ZRid | room_name | email | event_id | change_key | api_type
    logger.info(
        "%s | %s | %s | %s | %s | %s | %s | %s | %s",
        check_out.event,
        check_out.event_ts,
        check_out.payload.account_id,
        check_out.payload.object.id,
        check_out.payload.object.room_name,
        check_out.payload.object.email,
        check_out.payload.object.event_id,
        check_out.payload.object.change_key,
        check_out.payload.object.api_type,
    )

    # TODO: Add code here to handle the checked_out event.

    return ResponseWebhookCheckedOut(
        message="Checked out!",
    )
