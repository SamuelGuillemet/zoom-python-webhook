import logging

from .schema import CheckedInWebHook, ResponseWebhookCheckedIn

logger = logging.getLogger("app.components.zoomroom.checked_in")


def checked_in_handler(body: dict):
    check_in = CheckedInWebHook(**body)

    logger.info(
        "New checked_in event in room %s [%s] associated to %s, for event %s.",
        check_in.payload.object.room_name,
        check_in.payload.object.id,
        check_in.payload.object.resource_email,
        check_in.payload.object.event_id,
    )

    # TODO: Add code here to handle the checked_in event.

    return ResponseWebhookCheckedIn(
        message="Checked in!",
    )
