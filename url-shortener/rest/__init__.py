from fastapi import APIRouter

from rest.main_views import router as main_views_router
from rest.short_urls import router as short_urls_views_router

router = APIRouter(
    include_in_schema=False,
)
router.include_router(main_views_router)
router.include_router(short_urls_views_router)
