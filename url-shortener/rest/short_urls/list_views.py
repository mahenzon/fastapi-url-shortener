from typing import Any

from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from dependencies.short_urls import GetShortUrlsStorage
from templating import templates

router = APIRouter()


@router.get(
    "/",
    name="short-urls:list",
    response_class=HTMLResponse,
)
def list_view(
    request: Request,
    storage: GetShortUrlsStorage,
) -> HTMLResponse:
    context: dict[str, Any] = {}
    short_urls = storage.get()
    context.update(
        short_urls=short_urls,
    )
    return templates.TemplateResponse(
        request=request,
        name="short-urls/list.html",
        context=context,
    )
