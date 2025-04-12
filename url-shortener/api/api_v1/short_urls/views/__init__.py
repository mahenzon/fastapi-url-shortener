__all__ = ("router",)

from .details_views import router as details_router
from .list_views import router

router.include_router(details_router)
