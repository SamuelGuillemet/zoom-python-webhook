""" Logging configuration for the application. """

import logging
import sys
from datetime import datetime
from time import struct_time
from typing import Optional

from pytz import timezone, utc

from app.core.config import settings


def zurich_time(*args) -> struct_time:  # pylint: disable=unused-argument
    """
    Converts the current UTC time to the timezone of Zurich, Switzerland.

    Returns:
        A time tuple representing the current time in Zurich.
    """
    utc_dt = utc.localize(datetime.utcnow())
    my_tz = timezone("Europe/Zurich")
    converted = utc_dt.astimezone(my_tz)
    return converted.timetuple()


def setup_logs(logger_name: str, to_stdout: bool = True):
    """
    Sets up the logger with the specified logger name and configures it to log to stdout if `to_stdout` is True.
    The logger's log level is set based on the `LOG_LEVEL` value in the application's settings.

    Args:
        logger_name (str): The name of the logger.
        to_stdout (bool, optional): Whether to log to stdout. Defaults to True.
    """
    logger = logging.getLogger(logger_name)

    logger.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(
        "%(levelname)s | %(asctime)s | %(name)s | %(message)s | %(pathname)s:%(lineno)d | %(funcName)s()"
    )

    logging.Formatter.converter = zurich_time

    if to_stdout:
        configure_stdout_logging(
            logger=logger, formatter=formatter, log_level=settings.LOG_LEVEL
        )


def configure_stdout_logging(
    logger: Optional[logging.Logger] = None,
    formatter: Optional[logging.Formatter] = None,
    log_level: int = logging.DEBUG,
):
    """
    Configures the logger to log to stdout with the specified logger, formatter and log level.

    Args:
        logger (Optional[logging.Logger], optional): The logger to configure. Defaults to None.
        formatter (Optional[logging.Formatter], optional): The formatter to use. Defaults to None.
        log_level (str, optional): The log level to use. Defaults to "DEV".
    """
    stream_handler = logging.StreamHandler(stream=sys.stdout)

    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(log_level)

    if logger:
        logger.addHandler(stream_handler)
        print(f"Logging {str(logger)} to stdout -> True")
