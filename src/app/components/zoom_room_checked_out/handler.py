import logging

from .schema import CheckedOutWebHook, ResponseWebhookCheckedOut

logger = logging.getLogger("app.components.zoomroom.checked_out")


def checked_out_handler(body: dict):
    check_out = CheckedOutWebHook(**body)

    logger.info(
        "New checked_out event in room %s [%s] associated to %s, for event %s.",
        check_out.payload.object.room_name,
        check_out.payload.object.id,
        check_out.payload.object.resource_email,
        check_out.payload.object.event_id,
    )

    # TODO: Add code here to handle the checked_out event.

    return ResponseWebhookCheckedOut(
        message="Checked out!",
    )
