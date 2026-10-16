from fastapi import Header, HTTPException


def obtener_sub_actual(x_usuario_sub: str = Header(default="")) -> str:
    """Extrae el 'sub' del header que pone el BFF.

    PROVISIONAL (Fase 1): confia ciegamente en X-Usuario-Sub, igual que
    ms-condominios y ms-espacios-comunes hoy -- mismo riesgo ya documentado
    (header falsificable si el servicio queda expuesto sin pasar por el BFF).
    La Fase 2 debe resolver esto segun la alternativa A/B/C elegida en el
    diseno de autorizacion; esta funcion es el unico punto que cambiaria.
    """
    sub = x_usuario_sub.strip()
    if not sub:
        raise HTTPException(status_code=401, detail="Identidad de usuario faltante")
    return sub
