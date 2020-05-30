import pytest
from starlette.testclient import TestClient

from src.app.main import app


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def prefix():
    # TODO read this in from main.py or something
    return "/api/v1"
