from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.api_v1.short_urls.crud import storage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # действия до запуска приложения
    storage.init_storage_from_state()
    # ставим эту функцию на паузу на время работы приложения
    yield
    # выполняем завершение работы,
    # закрываем соединения, финально сохраняем файлы.
