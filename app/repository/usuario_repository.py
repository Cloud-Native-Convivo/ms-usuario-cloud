from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.usuario import Usuario


class UsuarioRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_sub_identidad(self, sub_identidad: str) -> Usuario | None:
        """Busca por sub_identidad normalizado a minusculas (Entra/Cognito no
        garantizan casing estable entre logins del mismo usuario)."""
        normalizado = sub_identidad.strip().lower()
        stmt = select(Usuario).where(Usuario.sub_identidad == normalizado)
        resultado = await self.session.execute(stmt)
        return resultado.scalars().first()
