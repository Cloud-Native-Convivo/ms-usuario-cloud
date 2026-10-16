class UsuarioException(Exception):
    pass


class UsuarioNoEncontradoException(UsuarioException):
    def __init__(self, sub_identidad: str):
        self.sub_identidad = sub_identidad
        super().__init__(f"Usuario con identidad '{sub_identidad}' no encontrado")
