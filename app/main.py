import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import py_eureka_client.eureka_client as eureka_client
from fastapi import FastAPI

from app.api.usuario_router import router as usuario_router
from app.config.settings import settings
from app.exception.usuario_exception import UsuarioNoEncontradoException
from app.handler.exception_handler import usuario_no_encontrado_handler
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.security_middleware import SecurityMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    if settings.eureka_url:
        try:
            await eureka_client.init_async(
                eureka_server=settings.eureka_url,
                app_name="ms-usuario-cloud",
                instance_port=settings.puerto,
                instance_ip=settings.eureka_ip,
                instance_host="ms-usuario-cloud",
            )
            logger.info("Registrado en Eureka")
        except Exception as error:
            logger.warning("Eureka no disponible (%s) — continuando", error)

    try:
        yield
    finally:
        if settings.eureka_url:
            try:
                await eureka_client.stop_async()
            except Exception as error:
                logger.warning("Error al desregistrar de Eureka: %s", error)


app = FastAPI(title="MS Usuario", lifespan=lifespan)

app.add_middleware(SecurityMiddleware)
app.add_middleware(LoggingMiddleware)

app.add_exception_handler(UsuarioNoEncontradoException, usuario_no_encontrado_handler)
app.include_router(usuario_router)
