from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from storage.short_urls import ShortUrlsStorage


@asynccontextmanager
async def lifespan(
    app: FastAPI,
) -> AsyncIterator[None]:
    # действия до запуска приложения
    # noinspection PyUnresolvedReferences
    app.state.short_urls_storage = ShortUrlsStorage(
        hash_name=settings.redis.collections_names.short_urls_hash,
    )
    # ставим эту функцию на паузу на время работы приложения
    yield
    # выполняем завершение работы,
    # закрываем соединения, финально сохраняем файлы.
