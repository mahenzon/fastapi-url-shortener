from fastapi import APIRouter

from rest.short_urls.list_views import router as list_views_router

router = APIRouter(
    prefix="/short-urls",
)
router.include_router(list_views_router)
