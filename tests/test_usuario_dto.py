from app.dto.usuario_dto import UsuarioRespuesta


def test_usuario_respuesta_se_construye_desde_atributos():
    class FalsoUsuario:
        id = 1
        sub_identidad = "abc-123"
        proveedor_identidad = "cognito"
        nombre = "Ana"
        correo = "ana@example.com"
        activo = True

    dto = UsuarioRespuesta.model_validate(FalsoUsuario())
    assert dto.sub_identidad == "abc-123"
    assert dto.activo is True
