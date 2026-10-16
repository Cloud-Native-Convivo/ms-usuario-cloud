from fastapi import Request
from fastapi.responses import JSONResponse

from app.exception.usuario_exception import UsuarioNoEncontradoException


def usuario_no_encontrado_handler(_request: Request, exc: UsuarioNoEncontradoException):
    return JSONResponse(status_code=404, content={"message": str(exc)})
