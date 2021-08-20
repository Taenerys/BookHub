import os.path
import sys
import pytest

from app import create_app

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

flask_app = create_app()


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
