""" Application configuration"""

import logging
import os
from functools import lru_cache
from typing import Optional

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger("app.core.config")

TEST_ZOOM_WEBHOOK_SECRET_TOKEN = "c9d1eea481f41908e56b39"


class Settings(BaseSettings):
    """Base class for application settings."""

    API_V1_PREFIX: str = "/api/v1"
    ZOOM_WEBHOOK_SECRET_TOKEN: str
    LOG_LEVEL: int

    model_config = SettingsConfigDict(case_sensitive=True)

    @field_validator("ZOOM_WEBHOOK_SECRET_TOKEN")
    def check_token(cls, v):
        """Raise a ValidationError if ZOOM_WEBHOOK_SECRET_TOKEN is None or empty."""
        if v is None or v == "":
            raise ValueError("ZOOM_WEBHOOK_SECRET_TOKEN is required")
        return v


class ConfigDevelopment(Settings):
    """
    Class for development environment configuration settings.
    Inherits from Settings class.
    Uses .env.development file for configuration of ZOOM_WEBHOOK_SECRET_TOKEN.
    """

    ZOOM_WEBHOOK_SECRET_TOKEN: Optional[str] = None
    LOG_LEVEL: int = logging.DEBUG

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env.development")


class ConfigProduction(Settings):
    """
    Class for production environment configuration settings.
    Inherits from Settings class.
    """

    ZOOM_WEBHOOK_SECRET_TOKEN: Optional[str] = None
    LOG_LEVEL: int = logging.INFO

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env.production")


class ConfigTest(Settings):
    """
    Class for test environment configuration settings.
    Inherits from Settings class.
    Uses TEST_ZOOM_WEBHOOK_SECRET_TOKEN for configuration of ZOOM_WEBHOOK_SECRET_TOKEN.
    """

    ZOOM_WEBHOOK_SECRET_TOKEN: str = TEST_ZOOM_WEBHOOK_SECRET_TOKEN
    LOG_LEVEL: int = logging.DEBUG


env = os.getenv("ENVIRONMENT", "development")


@lru_cache()
def get_settings(_env: Optional[str] = env) -> Settings:
    """
    Returns the application settings based on the environment specified.

    Args:
        _env (Optional[str], optional): Environment to get the settings for. Defaults to env.

    Raises:
        ValueError: If an invalid environment is specified.

    Returns:
        Settings: The application settings.
    """
    logger.info("Running in %s environment", env)
    _settings: Settings
    if _env == "development":
        _settings = ConfigDevelopment()
    elif _env == "production":
        _settings = ConfigProduction()
    elif _env == "test":
        _settings = ConfigTest()
    else:
        raise ValueError(f"Invalid environment {_env}")

    return _settings


settings = get_settings()
