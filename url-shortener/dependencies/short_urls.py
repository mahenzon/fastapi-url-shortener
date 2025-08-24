from typing import Annotated

from fastapi import Depends

from core.config import settings
from storage.short_urls import ShortUrlsStorage


def get_short_urls_storage() -> ShortUrlsStorage:
    return ShortUrlsStorage(
        hash_name=settings.redis.collections_names.short_urls_hash,
    )


GetShortUrlsStorage = Annotated[
    ShortUrlsStorage,
    Depends(get_short_urls_storage),
]
