from fastapi import APIRouter, Request, status
from starlette.responses import RedirectResponse

from dependencies.short_urls import (
    GetShortUrlsStorage,
    ShortUrlBySlug,
)

router = APIRouter(
    prefix="/{slug}/delete",
)


@router.post(
    "/",
    name="short-urls:delete",
)
async def delete_short_url(
    request: Request,
    short_url: ShortUrlBySlug,
    storage: GetShortUrlsStorage,
) -> RedirectResponse:
    storage.delete(short_url)
    return RedirectResponse(
        url=request.url_for("short-urls:list"),
        status_code=status.HTTP_303_SEE_OTHER,
    )
