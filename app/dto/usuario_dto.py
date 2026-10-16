from pydantic import BaseModel, ConfigDict


class UsuarioRespuesta(BaseModel):
    id: int
    sub_identidad: str
    proveedor_identidad: str
    nombre: str | None
    correo: str | None
    activo: bool
    model_config = ConfigDict(from_attributes=True)
