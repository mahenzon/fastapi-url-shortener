from datetime import date, datetime

from fastapi import Request
from fastapi.templating import Jinja2Templates

from core.config import BASE_DIR
from misc.flash_messages import get_flashed_messages


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
templates.env.globals[get_flashed_messages.__name__] = get_flashed_messages
