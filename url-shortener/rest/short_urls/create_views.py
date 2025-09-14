from fastapi import APIRouter, Request, status
from pydantic import ValidationError
from starlette.responses import HTMLResponse, RedirectResponse

from dependencies.short_urls import GetShortUrlsStorage
from schemas.short_url import ShortUrlCreate
from services.short_urls import FormResponseHelper
from storage.short_urls.exceptions import ShortUrlAlreadyExistsError

router = APIRouter(
    prefix="/create",
)

form_response = FormResponseHelper(
    model=ShortUrlCreate,
    template_name="short-urls/create.html",
)


@router.get(
    "/",
    name="short-urls:create-view",
)
def get_page_create_short_url(
    request: Request,
) -> HTMLResponse:
    return form_response.render(request)


@router.post(
    "/",
    name="short-urls:create",
    response_model=None,
)
async def create_short_url(
    request: Request,
    storage: GetShortUrlsStorage,
) -> RedirectResponse | HTMLResponse:
    async with request.form() as form:
        try:
            short_url_create = ShortUrlCreate.model_validate(form)
        except ValidationError as e:
            return form_response.render(
                request=request,
                form_data=form,
                pydantic_error=e,
                form_validated=True,
            )

    try:
        storage.create_or_raise_if_exists(
            short_url_create,
        )
    except ShortUrlAlreadyExistsError:
        errors = {
            "slug": f"Short url with slug {short_url_create.slug!r} already exists.",
        }
    else:
        request.session["message"] = (
            f"Last created short url with slug {short_url_create.slug!r}."
        )
        return RedirectResponse(
            url=request.url_for("short-urls:list"),
            status_code=status.HTTP_303_SEE_OTHER,
        )

    return form_response.render(
        request=request,
        errors=errors,
        form_data=short_url_create,
        form_validated=True,
    )
