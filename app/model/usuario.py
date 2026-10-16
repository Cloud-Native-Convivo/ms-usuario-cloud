from sqlalchemy import Boolean, Column, Identity, Integer, String, UniqueConstraint

from app.config.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = (
        UniqueConstraint("sub_identidad", name="uq_usuario_sub_identidad"),
    )

    id = Column(Integer, Identity(), primary_key=True)
    # Las LECTURAS se normalizan a minusculas en el repositorio (Task 6): Cognito/Entra
    # no garantizan casing estable del 'sub'/'oid' entre logins del mismo usuario. Esta
    # fase no tiene flujo de alta (no hay endpoint de escritura), asi que el ALMACENADO
    # no esta normalizado todavia -- Fase 2 debe normalizar tambien al crear el registro
    # (o agregar una validacion/constraint), o un sub guardado con mayusculas quedaria
    # inaccesible para siempre via el lookup normalizado.
    sub_identidad = Column(String(255), nullable=False)
    proveedor_identidad = Column(String(20), nullable=False)  # 'cognito' | 'entra'
    nombre = Column(String(255), nullable=True)
    correo = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)
