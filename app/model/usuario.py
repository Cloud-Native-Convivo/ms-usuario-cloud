from sqlalchemy import Boolean, Column, Identity, Integer, String, UniqueConstraint

from app.config.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = (
        UniqueConstraint("sub_identidad", name="uq_usuario_sub_identidad"),
    )

    id = Column(Integer, Identity(), primary_key=True)
    # Normalizado a minusculas en el repositorio (Task 6): Cognito/Entra no garantizan
    # casing estable del 'sub'/'oid' entre logins del mismo usuario.
    sub_identidad = Column(String(255), nullable=False)
    proveedor_identidad = Column(String(20), nullable=False)  # 'cognito' | 'entra'
    nombre = Column(String(255), nullable=True)
    correo = Column(String(255), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)
