from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Identity,
    Index,
    Integer,
    String,
    UniqueConstraint,
)

from app.config.database import Base


class UsuarioCondominioRol(Base):
    __tablename__ = "usuario_condominio_rol"
    __table_args__ = (
        Index("ix_ucr_usuario_id", "usuario_id"),
        Index("ix_ucr_condominio_id", "condominio_id"),
        # unidad_id puede ser NULL (ej. administrador de todo el condominio, no de una
        # unidad especifica). En Oracle, un UniqueConstraint compuesto solo deja pasar
        # duplicados cuando TODAS sus columnas son NULL -- con una sola columna NULL
        # (unidad_id) y el resto igual, dos filas SI colisionan (ORA-00001). Es el
        # comportamiento deseado: evita duplicar el mismo rol "de todo el condominio"
        # para el mismo usuario. Riesgo conocido, no ejercitado por repositorio/servicio
        # en esta fase -- ver "Riesgos conocidos y alcance explicitamente diferido" del plan.
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
