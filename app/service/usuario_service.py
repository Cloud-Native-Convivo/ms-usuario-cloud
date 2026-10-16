from app.exception.usuario_exception import UsuarioNoEncontradoException
from app.model.usuario import Usuario
from app.repository.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def obtener_por_sub(self, sub_identidad: str) -> Usuario:
        """Decision explicita de Fase 1: NO auto-crea el Usuario si no existe,
        lanza 404 en su lugar. Crear un Usuario es responsabilidad de un flujo
        de alta que Fase 2 debe definir, no de este GET."""
        usuario = await self.repository.get_by_sub_identidad(sub_identidad)
        if not usuario:
            raise UsuarioNoEncontradoException(sub_identidad)
        return usuario
