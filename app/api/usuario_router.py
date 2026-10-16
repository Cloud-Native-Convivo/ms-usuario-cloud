from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import obtener_sesion
from app.dto.usuario_dto import UsuarioRespuesta
from app.middleware.auth_roles import obtener_sub_actual
from app.model.usuario import Usuario
from app.repository.usuario_repository import UsuarioRepository
from app.service.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_usuario_service(db: AsyncSession = Depends(obtener_sesion)) -> UsuarioService:
    return UsuarioService(UsuarioRepository(db))


@router.get("/me", response_model=UsuarioRespuesta)
async def obtener_perfil_propio(
    sub: str = Depends(obtener_sub_actual), service: UsuarioService = Depends(get_usuario_service)
) -> Usuario:
    return await service.obtener_por_sub(sub)
