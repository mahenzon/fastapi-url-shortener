from typing import Annotated, Any

from fastapi import APIRouter, Form, Request
from starlette.responses import HTMLResponse

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
    short_url_create: Annotated[
        ShortUrlCreate,
        Form(),
    ],
) -> dict[str, str]:
    return short_url_create.model_dump(mode="json")
