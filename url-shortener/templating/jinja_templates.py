from datetime import date, datetime

from fastapi import Request
from fastapi.templating import Jinja2Templates

from core.config import BASE_DIR


def inject_current_date_and_dt(
    request: Request,  # noqa: ARG001
) -> dict[str, date]:
    return {
        "today": date.today(),
        "now": datetime.now(),
    }


templates = Jinja2Templates(
    directory=BASE_DIR / "templates",
    context_processors=[
        inject_current_date_and_dt,
    ],
)
