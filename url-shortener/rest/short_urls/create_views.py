from typing import Annotated, Any

from fastapi import APIRouter, Form, Request, status
from starlette.responses import HTMLResponse, RedirectResponse

from dependencies.short_urls import GetShortUrlsStorage
from schemas.short_url import ShortUrlCreate
from storage.short_urls.exceptions import ShortUrlAlreadyExistsError
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
    response_model=None,
)
def create_short_url(
    request: Request,
    short_url_create: Annotated[
        ShortUrlCreate,
        Form(),
    ],
    storage: GetShortUrlsStorage,
) -> RedirectResponse | HTMLResponse:
    try:
        storage.create_or_raise_if_exists(
            short_url_create,
        )
    except ShortUrlAlreadyExistsError:
        errors = {
            "slug": f"Short url with slug {short_url_create.slug!r} already exists.",
        }
    else:
        return RedirectResponse(
            url=request.url_for("short-urls:list"),
            status_code=status.HTTP_303_SEE_OTHER,
        )

    context: dict[str, Any] = {}
    model_schema = ShortUrlCreate.model_json_schema()
    context.update(
        model_schema=model_schema,
        form_validated=True,
        errors=errors,
        form_data=short_url_create,
    )
    return templates.TemplateResponse(
        request=request,
        name="short-urls/create.html",
        context=context,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
