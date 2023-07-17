""" Zoom Room Checked Out Component"""

from .handler import checked_out_handler
from .schema import ResponseWebhookCheckedOut

event_name = "zoomroom.checked_out"
handler_function = checked_out_handler
response_model = ResponseWebhookCheckedOut
