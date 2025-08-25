from fastapi import APIRouter
from starlette.responses import RedirectResponse

from dependencies.short_urls import ShortUrlBySlug

router = APIRouter(
    prefix="/r/{slug}",
    tags=["Redirect"],
)


@router.get("")
@router.get("/")
def redirect_short_url(
    url: ShortUrlBySlug,
) -> RedirectResponse:
    return RedirectResponse(
        url=str(url.target_url),
    )
