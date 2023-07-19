import logging

from .schema import ResponseWebhookSensorData, SensorDataWebHook

logger = logging.getLogger("app.components.zoomroom.sensor_data")


def sensor_data_handler(body: dict):
    sensor_data = SensorDataWebHook(**body)

    logger.debug(
        "New sensor data event in room %s [%s]. Reports %s sensors.",
        sensor_data.payload.object.room_name,
        sensor_data.payload.object.id,
        len(sensor_data.payload.object.sensor_data),
    )

    try:
        sensor_data.payload.object.sensor_data[0]
    except IndexError:
        logger.warning("No sensor data in the payload.")
        return ResponseWebhookSensorData(message="No sensor data in the payload.")

    for _, sensor in enumerate(sensor_data.payload.object.sensor_data):
        logger.info(
            "%s | %s | %s | %s | %s | %s | %s | %s",
            sensor_data.event,
            sensor_data.event_ts,
            sensor_data.payload.account_id,
            sensor_data.payload.object.id,
            sensor_data.payload.object.room_name,
            sensor.sensor_type.value,
            sensor.sensor_value,
            sensor.date_time,
        )

    # TODO: Add code here to handle the sensor_data event.

    return ResponseWebhookSensorData(message="Sensor data event received.")
