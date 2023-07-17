import pytest
from pydantic import ValidationError

from app.core.config import (
    TEST_ZOOM_WEBHOOK_SECRET_TOKEN,
    ConfigDevelopment,
    ConfigProduction,
    ConfigTest,
    get_settings,
)


def test_field_null(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ZOOM_WEBHOOK_SECRET_TOKEN", "")
    with pytest.raises(ValidationError) as excinfo:
        ConfigProduction()

    assert (
        excinfo.value.errors()[0]["msg"]
        == "Value error, ZOOM_WEBHOOK_SECRET_TOKEN is required"
    )


def test_env_dev(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ZOOM_WEBHOOK_SECRET_TOKEN", "FAKE_VALUE")

    assert isinstance(get_settings("development"), ConfigDevelopment)


def test_env_prod(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ZOOM_WEBHOOK_SECRET_TOKEN", "FAKE_VALUE")

    assert isinstance(get_settings("production"), ConfigProduction)


def test_env_test():
    settings = get_settings("test")
    assert isinstance(settings, ConfigTest)
    assert settings.ZOOM_WEBHOOK_SECRET_TOKEN == TEST_ZOOM_WEBHOOK_SECRET_TOKEN


def test_env_invalid():
    with pytest.raises(ValueError) as excinfo:
        get_settings("invalid")

    assert excinfo.value.args[0] == "Invalid environment invalid"
