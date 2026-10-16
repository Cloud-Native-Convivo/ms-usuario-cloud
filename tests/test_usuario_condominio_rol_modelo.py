from app.model.usuario_condominio_rol import UsuarioCondominioRol


def test_columnas_esperadas_para_la_fase_2():
    columnas = {c.name for c in UsuarioCondominioRol.__table__.columns}
    assert columnas == {"id", "usuario_id", "condominio_id", "unidad_id", "rol", "activo"}
    # unidad_id debe admitir NULL: un administrador de todo el condominio, no de
    # una unidad especifica, es un estado valido (no se construye el repositorio
    # que lo ejercita en esta fase, pero el esquema debe permitirlo desde ya).
    assert UsuarioCondominioRol.__table__.columns["unidad_id"].nullable is True

    constraints_unicos = [
        c for c in UsuarioCondominioRol.__table__.constraints
        if c.__class__.__name__ == "UniqueConstraint"
    ]
    assert len(constraints_unicos) == 1
    columnas_del_unique = {col.name for col in constraints_unicos[0].columns}
    assert columnas_del_unique == {"usuario_id", "condominio_id", "unidad_id", "rol"}
