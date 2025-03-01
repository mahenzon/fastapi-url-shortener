from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel, AnyHttpUrl


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl
    description: Annotated[
        str,
        MaxLen(200),
    ] = ""


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращённой ссылки
    """

    # noinspection PyTypeHints
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]


class ShortUrlUpdate(ShortUrlBase):
    """
    Модель для обновления информации о сокращенной ссылке
    """

    description: Annotated[
        str,
        MaxLen(200),
    ]


class ShortUrl(ShortUrlBase):
    """
    Модель сокращённой ссылки
    """

    slug: str
