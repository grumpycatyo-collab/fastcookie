"""Configuration handling."""

import os
from pathlib import Path

import yaml

from .settings import Settings

BASE_DIR = Path(__file__).resolve().parent.parent


def get_config() -> dict:
    """Load config from YAML file."""
    config_path = os.environ.get("CONFIG_PATH", BASE_DIR / "config.yml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def get_settings() -> Settings:
    """Get application settings."""
    config = get_config()
    return Settings(config=config)
