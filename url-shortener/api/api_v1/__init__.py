from fastapi import APIRouter

from .short_urls.views import router as short_urls_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(short_urls_router)
