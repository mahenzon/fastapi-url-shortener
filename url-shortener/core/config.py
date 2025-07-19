import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class LoggingConfig(BaseModel):
    log_level_name: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"
    log_format: str = LOG_FORMAT
    date_format: str = "%Y-%m-%d %H:%M:%S"

    @property
    def log_level(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level_name]


class RedisConnectionConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379


class RedisDatabaseConfig(BaseModel):
    default: int = 0
    tokens: int = 1
    users: int = 2
    short_urls: int = 3


class RedisCollectionsNamesConfig(BaseModel):
    tokens_set: str = "tokens"
    short_urls_hash: str = "short-urls"


class RedisConfig(BaseModel):
    connection: RedisConnectionConfig = RedisConnectionConfig()
    db: RedisDatabaseConfig = RedisDatabaseConfig()
    collections_names: RedisCollectionsNamesConfig = RedisCollectionsNamesConfig()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        cli_parse_args=True,
        case_sensitive=False,
    )
    logging: LoggingConfig = LoggingConfig()
    redis: RedisConfig = RedisConfig()


# noinspection PyArgumentList
settings = Settings()
