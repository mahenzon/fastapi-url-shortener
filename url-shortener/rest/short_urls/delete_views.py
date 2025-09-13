from fastapi import APIRouter, Request, status
from starlette.responses import RedirectResponse

router = APIRouter(
    prefix="/{slug}/delete",
)


@router.post(
    "/",
    name="short-urls:delete",
)
async def delete_short_url(
    request: Request,
) -> RedirectResponse:
    return RedirectResponse(
        url=request.url_for("short-urls:list"),
        status_code=status.HTTP_303_SEE_OTHER,
    )
