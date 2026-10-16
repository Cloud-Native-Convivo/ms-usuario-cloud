import pytest

from app.exception.usuario_exception import UsuarioNoEncontradoException
from app.model.usuario import Usuario
from app.service.usuario_service import UsuarioService


@pytest.mark.asyncio
async def test_obtener_por_sub_existente(mock_usuario_repo):
    usuario = Usuario(id=1, sub_identidad="abc-123", proveedor_identidad="cognito")
    mock_usuario_repo.get_by_sub_identidad.return_value = usuario
    service = UsuarioService(mock_usuario_repo)

    resultado = await service.obtener_por_sub("abc-123")

    assert resultado is usuario


@pytest.mark.asyncio
async def test_obtener_por_sub_inexistente_lanza_excepcion(mock_usuario_repo):
    mock_usuario_repo.get_by_sub_identidad.return_value = None
    service = UsuarioService(mock_usuario_repo)

    with pytest.raises(UsuarioNoEncontradoException):
        await service.obtener_por_sub("no-existe")
