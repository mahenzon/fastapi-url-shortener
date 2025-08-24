from fastapi import APIRouter

from rest.main_views import router as main_views_router

router = APIRouter(
    include_in_schema=False,
)
router.include_router(main_views_router)
