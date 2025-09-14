from typing import TypedDict

from fastapi import Request

FLASHED_MESSAGES_KEY = "_flashed_messages"


class Message(TypedDict):
    message: str
    category: str


def flash(request: Request, message: str, category: str = "info") -> None:
    if FLASHED_MESSAGES_KEY not in request.session:
        request.session[FLASHED_MESSAGES_KEY] = []
    request.session[FLASHED_MESSAGES_KEY].append(
        Message(
            message=message,
            category=category,
        ),
    )


def get_flashed_messages(
    request: Request,
) -> list[Message]:
    return request.session.pop(FLASHED_MESSAGES_KEY, [])
