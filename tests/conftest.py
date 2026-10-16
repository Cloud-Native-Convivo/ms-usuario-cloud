import os

os.environ.setdefault("DB_PASSWORD", "test")

from unittest.mock import AsyncMock  # noqa: E402

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: E402

from app.main import app  # noqa: E402


@pytest.fixture
def mock_session():
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


from app.repository.usuario_repository import UsuarioRepository


@pytest.fixture
def mock_usuario_repo():
    return AsyncMock(spec=UsuarioRepository)


from app.service.usuario_service import UsuarioService


@pytest.fixture
def mock_usuario_service():
    return AsyncMock(spec=UsuarioService)


from app.api.usuario_router import get_usuario_service


@pytest.fixture
def client_usuario(mock_usuario_service):
    app.dependency_overrides[get_usuario_service] = lambda: mock_usuario_service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
