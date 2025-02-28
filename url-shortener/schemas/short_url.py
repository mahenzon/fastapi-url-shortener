from pydantic import BaseModel


class ShortUrlBase(BaseModel):
    target_url: str
    slug: str


class ShortUrl(ShortUrlBase):
    """
    Модель сокращённой ссылки
    """
