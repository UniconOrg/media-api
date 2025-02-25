# Standard Library
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv

# Third Party Stuff
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict

from shared.app.environment import EnvironmentsTypes

LIST_PATH_TO_ADD = []
if LIST_PATH_TO_ADD:
    sys.path.extend(LIST_PATH_TO_ADD)


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENVS_DIR = BASE_DIR.parent / ".envs"
ENV_BASE_FILE_PATH = ENVS_DIR / ".env.base"
load_dotenv(ENV_BASE_FILE_PATH)
ENVIRONMENT = os.environ.get("ENVIRONMENT")
EnvironmentsTypes.validate(ENVIRONMENT)
ENV_FILE_PATH = ENVS_DIR / EnvironmentsTypes.get_env_file_name(ENVIRONMENT)


class Settings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore", case_sensitive=True)
    ENVIRONMENT: str = ENVIRONMENT

    # Project Constants
    # ----------------------------------------------------------------
    PROJECT_NAME: str = "Media Upload"
    PROJECT_ID: str = "API0003"
    TEAM_NAME: str = "R2"
    TIME_ZONE: str = "utc"
    TIME_ZONE_UTC: str = "utc"
    DATE_FORMAT: str = "%Y-%m-%d"
    DATE_TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    API_V1: str = "v1"
    CORS_ORIGINS: ClassVar[list[str]] = ["*"]
    SHOW_CRUDS_IN_SWAGGER_SCHEMA: bool = False

    # Database settings
    # ----------------------------------------------------------------
    POSTGRES_DSN: PostgresDsn | None


    # Sentry settings
    # ----------------------------------------------------------------
    SENTRY_DSN: str

    # WebHook
    # ----------------------------------------------------------------
    WEBHOOK: str
    WEBHOOK_SIGNALS: list[str] = [
        "/api/v1/exmaples/*",
    ]

    RESOURCE_API: list[str] = [
        "/api",
        "/health"
    ]

    PRIVATE_KEY_JWT: str

    # Pagination settings
    # ----------------------------------------------------------------
    DEFAULT_PAGE_SIZE: int = 30
    DEFAULT_ORDER_FIELD: str = "created"
    TIMESTAP: datetime = datetime.now().astimezone().strftime(format=DATE_TIME_FORMAT)