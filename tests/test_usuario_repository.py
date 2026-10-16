from unittest.mock import AsyncMock, MagicMock

import pytest

from app.model.usuario import Usuario
from app.repository.usuario_repository import UsuarioRepository


@pytest.mark.asyncio
async def test_get_by_sub_identidad_normaliza_a_minusculas(mock_session):
    usuario = Usuario(id=1, sub_identidad="abc-123", proveedor_identidad="cognito")
    resultado = MagicMock()
    resultado.scalars.return_value.first.return_value = usuario
    mock_session.execute = AsyncMock(return_value=resultado)
    repo = UsuarioRepository(mock_session)

    encontrado = await repo.get_by_sub_identidad("ABC-123")  # mayusculas a proposito

    assert encontrado is usuario
    stmt_ejecutado = mock_session.execute.call_args.args[0]
    # La comparacion debe hacerse sobre el valor normalizado (minusculas),
    # no sobre "ABC-123" tal cual vino.
    assert "abc-123" in str(stmt_ejecutado.compile(compile_kwargs={"literal_binds": True}))
