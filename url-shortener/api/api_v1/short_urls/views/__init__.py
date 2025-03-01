__all__ = ("router",)

from .list_views import router
from .details_views import router as details_router

router.include_router(details_router)
