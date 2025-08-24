from collections.abc import Generator

import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient
from pydantic import AnyHttpUrl

from main import app
from schemas.short_url import DESCRIPTION_MAX_LENGTH, ShortUrl, ShortUrlUpdate
from storage.short_urls.crud import storage
from testing.conftest import create_short_url_random_slug


@pytest.mark.apitest
class TestUpdate:

    @pytest.fixture()
    def short_url(self, request: SubRequest) -> Generator[ShortUrl]:
        description, url = request.param
        short_url = create_short_url_random_slug(
            description=description,
            target_url=url,
        )
        yield short_url
        storage.delete(short_url)

    @pytest.mark.parametrize(
        "short_url, new_description, new_target_url",
        [
            pytest.param(
                ("some description", "https://example.com"),
                "some description",
                "https://site.com",
                id="same-description-and-new-target-url",
            ),
            pytest.param(
                ("old description", "https://www.example.com"),
                "new description",
                "https://www.qwerty.com",
                id="new-description-and-new-target-url",
            ),
            pytest.param(
                ("basic description", "https://example.com"),
                "",
                "https://basic-site-name.com",
                id="empty-description-and-new-target-url",
            ),
            pytest.param(
                ("the description", "https://example.com"),
                "a" * DESCRIPTION_MAX_LENGTH,
                "https://example.com",
                id="max-description-and-same-target-url",
            ),
        ],
        indirect=["short_url"],
    )
    def test_update_short_url_details(
        self,
        short_url: ShortUrl,
        new_description: str,
        new_target_url: str | AnyHttpUrl,
        auth_client: TestClient,
    ) -> None:
        url = app.url_path_for(
            "update_short_url_details",
            slug=short_url.slug,
        )
        update = ShortUrlUpdate(
            description=new_description,
            target_url=new_target_url,
        )
        response = auth_client.put(
            url,
            json=update.model_dump(mode="json"),
        )
        assert response.status_code == status.HTTP_200_OK, response.text
        short_url_db = storage.get_by_slug(short_url.slug)
        assert short_url_db
        new_data = ShortUrlUpdate(**short_url_db.model_dump())
        assert new_data == update
