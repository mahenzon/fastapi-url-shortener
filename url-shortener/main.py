import logging

from fastapi import (
    FastAPI,
)

from api import router as api_router
from api.main_views import router as main_router
from api.redirect_views import router as redirect_views
from app_lifespan import lifespan
from core import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)

app = FastAPI(
    title="URL Shortener",
    lifespan=lifespan,
)

app.include_router(main_router)
app.include_router(redirect_views)
app.include_router(api_router)
