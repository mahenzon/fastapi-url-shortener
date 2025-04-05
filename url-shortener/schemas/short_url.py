from typing import Annotated

from annotated_types import Len, MaxLen
from pydantic import BaseModel, AnyHttpUrl


DescriptionString = Annotated[
    str,
    MaxLen(200),
]


class ShortUrlBase(BaseModel):
    target_url: AnyHttpUrl
    description: DescriptionString


class ShortUrlCreate(ShortUrlBase):
    """
    Модель для создания сокращённой ссылки
    """

    # noinspection PyTypeHints
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    description: DescriptionString = ""


class ShortUrlUpdate(ShortUrlBase):
    """
    Модель для обновления информации о сокращенной ссылке
    """


class ShortUrlPartialUpdate(BaseModel):
    """
    Модель для частичного обновления информации
    о сокращенной ссылке
    """

    target_url: AnyHttpUrl | None = None
    description: DescriptionString | None = None


class ShortUrlRead(ShortUrlBase):
    """
    Модель для чтения данных по короткой ссылке.
    """

    slug: str
    description: str


class ShortUrl(ShortUrlBase):
    """
    Модель сокращённой ссылки
    """

    slug: str
    description: str
    visits: int = 42
