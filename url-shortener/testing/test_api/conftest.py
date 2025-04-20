from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from api.api_v1.auth.services import redis_tokens
from main import app


@pytest.fixture()
def client() -> Generator[TestClient]:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
def auth_token() -> Generator[str]:
    token = redis_tokens.generate_and_save_token()
    yield token
    redis_tokens.delete_token(token)


@pytest.fixture(scope="module")
def auth_client(
    auth_token: str,
) -> Generator[TestClient]:
    headers = {"Authorization": f"Bearer {auth_token}"}
    with TestClient(app, headers=headers) as client:
        yield client
