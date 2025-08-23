from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from core.config import BASE_DIR

router = APIRouter()


@router.get(
    "/",
    response_class=HTMLResponse,
)
def read_root() -> str:
    return (BASE_DIR / "pages" / "home.html").read_text()
