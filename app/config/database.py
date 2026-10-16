from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config.settings import settings


class Base(DeclarativeBase):
    pass


motor = create_async_engine(settings.url_base_datos)
fabrica_sesiones = async_sessionmaker(motor, expire_on_commit=False)


async def obtener_sesion() -> AsyncGenerator[AsyncSession, None]:
    async with fabrica_sesiones() as sesion:
        yield sesion
