from app.models.usuario import Usuario


def obtener_usuario_por_username(
    db,
    username
):

    return db.query(Usuario).filter(
        Usuario.usuario == username
    ).first()