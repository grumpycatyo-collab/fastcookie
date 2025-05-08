"""Application settings."""

from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    """Environment enum."""

    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


# TODO: Work on settings and config management (not good for now)
class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # From environment variables
    api_env: Environment = Field(default=Environment.DEVELOPMENT, env="API_ENV")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    secret_key: str = Field(default="default_insecure_key", env="SECRET_KEY")

    # From config.yml
    config: dict = {}

    @property
    def app_name(self) -> str:
        """Get application name."""
        return self.config.get("app", {}).get("name", "{{cookiecutter.project_name}}")

    @property
    def app_description(self) -> str:
        """Get application description."""
        return self.config.get("app", {}).get(
            "description", "{{cookiecutter.project_description}}"
        )

    @property
    def debug(self) -> bool:
        """Get debug mode."""
        return (
            self.config.get("environment", {}).get(self.api_env, {}).get("debug", False)
        )

    @property
    def cors_origins(self) -> list[str]:
        """Get CORS origins."""
        return (
            self.config.get("environment", {})
            .get(self.api_env, {})
            .get("cors_origins", [])
        )
