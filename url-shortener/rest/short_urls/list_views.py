from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from templating import templates

router = APIRouter()


@router.get(
    "/",
    name="short-urls:list",
    response_class=HTMLResponse,
)
def list_view(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="short-urls/list.html",
    )
