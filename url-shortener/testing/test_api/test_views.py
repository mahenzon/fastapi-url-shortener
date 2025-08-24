import pytest
from fastapi import status
from fastapi.testclient import TestClient

pytestmark = pytest.mark.tempaltetest


def test_root_view(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.template.name == "home.html"  # type: ignore[attr-defined]
    assert "features" in response.context, response.context  # type: ignore[attr-defined]
    assert isinstance(response.context["features"], list)  # type: ignore[attr-defined]
