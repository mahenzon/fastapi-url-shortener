from typing import Annotated, Any

from fastapi import APIRouter, Form, Request, status
from starlette.responses import HTMLResponse, RedirectResponse

from dependencies.short_urls import GetShortUrlsStorage
from schemas.short_url import ShortUrlCreate
from templating import templates

router = APIRouter(
    prefix="/create",
)


@router.get(
    "/",
    name="short-urls:create-view",
)
def get_page_create_short_url(
    request: Request,
) -> HTMLResponse:
    context: dict[str, Any] = {}
    model_schema = ShortUrlCreate.model_json_schema()
    context.update(
        model_schema=model_schema,
    )
    return templates.TemplateResponse(
        request=request,
        name="short-urls/create.html",
        context=context,
    )


@router.post(
    "/",
    name="short-urls:create",
)
def create_short_url(
    request: Request,
    short_url_create: Annotated[
        ShortUrlCreate,
        Form(),
    ],
    storage: GetShortUrlsStorage,
) -> RedirectResponse:
    storage.create_or_raise_if_exists(
        short_url_create,
    )
    return RedirectResponse(
        url=request.url_for("short-urls:list"),
        status_code=status.HTTP_303_SEE_OTHER,
    )
