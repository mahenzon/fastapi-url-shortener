"""
Create
Read
Update
Delete
"""

from pydantic import BaseModel, AnyHttpUrl

from schemas.short_url import (
    ShortUrl,
    ShortUrlCreate,
)


class ShortUrlsStorage(BaseModel):
    slug_to_short_url: dict[str, ShortUrl] = {}

    def get(self) -> list[ShortUrl]:
        return list(self.slug_to_short_url.values())

    def get_by_slug(self, slug: str) -> ShortUrl | None:
        return self.slug_to_short_url.get(slug)

    def create(self, short_url_in: ShortUrlCreate) -> ShortUrl:
        short_url = ShortUrl(
            **short_url_in.model_dump(),
        )
        self.slug_to_short_url[short_url.slug] = short_url
        return short_url


storage = ShortUrlsStorage()

storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://www.example.com"),
        slug="example",
    ),
)
storage.create(
    ShortUrlCreate(
        target_url=AnyHttpUrl("https://www.google.com"),
        slug="search",
    ),
)
