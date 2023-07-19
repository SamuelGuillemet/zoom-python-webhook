""" Zoom Room Sensor Data Component"""

from .handler import sensor_data_handler
from .schema import ResponseWebhookSensorData

event_name = "zoomroom.sensor_data"
handler_function = sensor_data_handler
response_model = ResponseWebhookSensorData
