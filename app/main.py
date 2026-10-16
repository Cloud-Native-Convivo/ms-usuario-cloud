import logging

from fastapi import FastAPI

from app.api.usuario_router import router as usuario_router
from app.exception.usuario_exception import UsuarioNoEncontradoException
from app.handler.exception_handler import usuario_no_encontrado_handler
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.security_middleware import SecurityMiddleware

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="MS Usuario")

app.add_middleware(SecurityMiddleware)
app.add_middleware(LoggingMiddleware)

app.add_exception_handler(UsuarioNoEncontradoException, usuario_no_encontrado_handler)
app.include_router(usuario_router)
