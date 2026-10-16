from app.dto.usuario_dto import UsuarioRespuesta
from app.exception.usuario_exception import UsuarioNoEncontradoException


def test_me_sin_header_da_401(client_usuario, mock_usuario_service):
    response = client_usuario.get("/usuarios/me")
    assert response.status_code == 401
    mock_usuario_service.obtener_por_sub.assert_not_called()


def test_me_exitoso(client_usuario, mock_usuario_service):
    mock_usuario_service.obtener_por_sub.return_value = UsuarioRespuesta(
        id=1, sub_identidad="abc-123", proveedor_identidad="cognito",
        nombre="Ana", correo="ana@example.com", activo=True,
    )
    response = client_usuario.get("/usuarios/me", headers={"X-Usuario-Sub": "abc-123"})
    assert response.status_code == 200
    assert response.json()["sub_identidad"] == "abc-123"
    mock_usuario_service.obtener_por_sub.assert_called_once_with("abc-123")


def test_me_usuario_no_registrado_da_404(client_usuario, mock_usuario_service):
    mock_usuario_service.obtener_por_sub.side_effect = UsuarioNoEncontradoException("abc-123")
    response = client_usuario.get("/usuarios/me", headers={"X-Usuario-Sub": "abc-123"})
    assert response.status_code == 404
