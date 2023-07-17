""" Endpoint URL Validation Component"""

from .handler import url_validation_handler
from .schema import ResponseWebhookUrlValidation

event_name = "endpoint.url_validation"
handler_function = url_validation_handler
response_model = ResponseWebhookUrlValidation
