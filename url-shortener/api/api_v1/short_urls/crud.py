"""
Create
Read
Update
Delete
"""

__all__ = (
    "ShortUrlAlreadyExistsError",
    "storage",
)

import logging
from collections.abc import Iterable
from typing import cast

from pydantic import BaseModel
from redis import Redis

from core.config import settings
from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
    ShortUrlPartialUpdate,
    ShortUrlUpdate,
)

log = logging.getLogger(__name__)

redis = Redis(
    host=settings.redis.connection.host,
    port=settings.redis.connection.port,
    db=settings.redis.db.short_urls,
    decode_responses=True,
)


class ShortUrlBaseError(Exception):
    """
    Base exception for short url CRUD actions.
    """


class ShortUrlAlreadyExistsError(ShortUrlBaseError):
    """
    Raised on short url creation if such slug already exists.
    """


class ShortUrlsStorage(BaseModel):
    hash_name: str

    def save_short_url(self, short_url: ShortUrl) -> None:
        redis.hset(
            name=self.hash_name,
            key=short_url.slug,
            value=short_url.model_dump_json(),
        )

    def get(self) -> list[ShortUrl]:
        return [
            ShortUrl.model_validate_json(value)
            for value in cast(
                Iterable[str],
                redis.hvals(name=self.hash_name),
            )
        ]

    def get_by_slug(self, slug: str) -> ShortUrl | None:
        if data := redis.hget(
            name=self.hash_name,
            key=slug,
        ):
            assert isinstance(data, str)
            return ShortUrl.model_validate_json(data)

        return None

    def exists(self, slug: str) -> bool:
        return cast(
            bool,
            redis.hexists(
                name=self.hash_name,
                key=slug,
            ),
        )

    def create(self, short_url_in: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_in.model_dump(),
        )
        self.save_short_url(short_url)
        log.info("Created short url %s", short_url)
        return short_url

    def create_or_raise_if_exists(self, short_url_in: ShortUrlCreate) -> ShortUrl:
        if not self.exists(short_url_in.slug):
            return self.create(short_url_in)

        raise ShortUrlAlreadyExistsError(short_url_in.slug)

    def delete_by_slug(self, slug: str) -> None:
        redis.hdel(
            self.hash_name,
            slug,
        )

    def delete(self, short_url: ShortUrl) -> None:
        self.delete_by_slug(slug=short_url.slug)

    def update(
        self,
        short_url: ShortUrl,
        short_url_in: ShortUrlUpdate,
    ) -> ShortUrl:
        for field_name, value in short_url_in:
            setattr(short_url, field_name, value)
        self.save_short_url(short_url)
        return short_url

    def update_partial(
        self,
        short_url: ShortUrl,
        short_url_in: ShortUrlPartialUpdate,
    ) -> ShortUrl:
        for field_name, value in short_url_in.model_dump(exclude_unset=True).items():
            setattr(short_url, field_name, value)
        self.save_short_url(short_url)
        return short_url


storage = ShortUrlsStorage(
    hash_name=settings.redis.collections_names.short_urls_hash,
)
