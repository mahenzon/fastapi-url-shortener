from typing import Annotated

from fastapi import (
    APIRouter,
    Form,
    Request,
    status,
)
from starlette.responses import (
    HTMLResponse,
    RedirectResponse,
)

from dependencies.short_urls import (
    GetShortUrlsStorage,
    ShortUrlBySlug,
)
from schemas.short_url import ShortUrlUpdateForm
from services.short_urls import FormResponseHelper

router = APIRouter(
    prefix="/{slug}/update",
)

form_response = FormResponseHelper(
    model=ShortUrlUpdateForm,
    template_name="short-urls/update.html",
)


@router.get(
    "/",
    name="short-urls:update-view",
)
def get_page_update_short_url(
    request: Request,
    short_url: ShortUrlBySlug,
) -> HTMLResponse:
    form = ShortUrlUpdateForm(**short_url.model_dump())
    return form_response.render(
        request=request,
        form_data=form,
        short_url=short_url,
    )


@router.post(
    "/",
    name="short-urls:update",
)
def update_short_url(
    request: Request,
    short_url: ShortUrlBySlug,
    short_url_in: Annotated[
        ShortUrlUpdateForm,
        Form(),
    ],
    storage: GetShortUrlsStorage,
) -> RedirectResponse:
    storage.update(
        short_url=short_url,
        short_url_in=short_url_in,
    )
    return RedirectResponse(
        url=request.url_for("short-urls:list"),
        status_code=status.HTTP_303_SEE_OTHER,
    )
