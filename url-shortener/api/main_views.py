from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from templating import templates

router = APIRouter()


@router.get(
    "/",
    name="home",
    include_in_schema=False,
)
def home_page(
    request: Request,
) -> HTMLResponse:
    context = {}
    features = [
        "Create short URLs",
        "Track all redirects",
        "Real-time statistics",
        "Shared management",
    ]
    context.update(
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context,
    )


@router.get(
    "/about/",
    name="about",
    include_in_schema=False,
)
def about_page(
    request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="about.html",
    )
