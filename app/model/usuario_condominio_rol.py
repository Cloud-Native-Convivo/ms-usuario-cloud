from sqlalchemy import Boolean, Column, ForeignKey, Identity, Index, Integer, String, UniqueConstraint

from app.config.database import Base


class UsuarioCondominioRol(Base):
    __tablename__ = "usuario_condominio_rol"
    __table_args__ = (
        Index("ix_ucr_usuario_id", "usuario_id"),
        Index("ix_ucr_condominio_id", "condominio_id"),
        # unidad_id puede ser NULL (ej. administrador de todo el condominio, no de una
        # unidad especifica) -- UniqueConstraint trata NULLs como distintos en Oracle,
        # asi que dos filas con unidad_id=NULL para el mismo (usuario,condominio,rol)
        # NO colisionan por si solas; es un caso valido, no un bug (ver Review Focus #3).
        UniqueConstraint("usuario_id", "condominio_id", "unidad_id", "rol", name="uq_ucr_asociacion"),
    )

    id = Column(Integer, Identity(), primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    # Sin FK real a ms-condominios: microservicio distinto, base distinta. Mismo
    # patron que ms-gastos-comunes.GastoComun.unidadId (referencia externa suelta).
    condominio_id = Column(Integer, nullable=False)
    unidad_id = Column(Integer, nullable=True)
    rol = Column(String(20), nullable=False)  # 'residente' | 'propietario' | 'administrador' | 'comite' | 'conserje'
    activo = Column(Boolean, nullable=False, default=True)
