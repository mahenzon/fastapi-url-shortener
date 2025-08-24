from typing import Annotated

from fastapi import APIRouter, Form

from schemas.short_url import ShortUrlCreate

router = APIRouter(
    prefix="/create",
)


@router.get(
    "/",
    name="short-urls:create-view",
)
def get_page_create_short_url() -> None:
    pass


@router.post(
    "/",
    name="short-urls:create",
)
def create_short_url(
    short_url_create: Annotated[
        ShortUrlCreate,
        Form(),
    ],
) -> dict[str, str]:
    return short_url_create.model_dump(mode="json")
