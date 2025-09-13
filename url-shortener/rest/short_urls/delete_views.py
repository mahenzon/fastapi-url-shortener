from fastapi import APIRouter, Response, status

from dependencies.short_urls import (
    GetShortUrlsStorage,
    ShortUrlBySlug,
)

router = APIRouter(
    prefix="/{slug}/delete",
)


@router.delete(
    "/",
    name="short-urls:delete",
)
async def delete_short_url(
    short_url: ShortUrlBySlug,
    storage: GetShortUrlsStorage,
) -> Response:
    storage.delete(short_url)
    return Response(
        status_code=status.HTTP_200_OK,
        content="",
    )
