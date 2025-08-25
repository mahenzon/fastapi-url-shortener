from typing import Annotated

from fastapi import Depends, HTTPException, Request
from starlette import status

from schemas.short_url import ShortUrl
from storage.short_urls import ShortUrlsStorage


def get_short_urls_storage(
    request: Request,
) -> ShortUrlsStorage:
    return request.app.state.short_urls_storage  # type: ignore[no-any-return]


GetShortUrlsStorage = Annotated[
    ShortUrlsStorage,
    Depends(get_short_urls_storage),
]


def prefetch_short_url(
    slug: str,
    storage: GetShortUrlsStorage,
) -> ShortUrl:
    url: ShortUrl | None = storage.get_by_slug(slug=slug)
    if url:
        return url

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"URL {slug!r} not found",
    )


ShortUrlBySlug = Annotated[
    ShortUrl,
    Depends(prefetch_short_url),
]
