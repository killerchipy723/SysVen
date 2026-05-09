from app.repositories.usuario_repository import obtener_usuario_por_username

from app.core.security import verify_password
from app.core.security import create_access_token


def login_usuario(
    db,
    username,
    password
):

    usuario = obtener_usuario_por_username(
        db,
        username
    )

    if not usuario:
        return None

    if not verify_password(
        password,
        usuario.password
    ):
        return None

    token = create_access_token({
        "sub": usuario.usuario
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }