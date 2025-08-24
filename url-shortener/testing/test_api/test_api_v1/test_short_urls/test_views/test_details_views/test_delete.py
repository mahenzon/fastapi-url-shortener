import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient

from main import app
from schemas.short_url import ShortUrl
from storage.short_urls.crud import storage
from testing.conftest import create_short_url


@pytest.fixture(
    params=[
        "some-slug",
        "slug",
        pytest.param("abc", id="minimal-slug"),
        pytest.param("qwerty-foo", id="max-slug"),
    ],
)
def short_url(request: SubRequest) -> ShortUrl:
    return create_short_url(request.param)


@pytest.mark.apitest
def test_delete(
    short_url: ShortUrl,
    auth_client: TestClient,
) -> None:
    url = app.url_path_for(
        "delete_short_url",
        slug=short_url.slug,
    )
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
    assert not storage.exists(short_url.slug)
