""" Zoom Room Checked In Component"""

from .handler import checked_in_handler
from .schema import ResponseWebhookCheckedIn

event_name = "zoomroom.checked_in"
handler_function = checked_in_handler
response_model = ResponseWebhookCheckedIn
