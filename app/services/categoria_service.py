from app.repositories.categoria_repository import crear_categoria
from app.repositories.categoria_repository import obtener_categorias


def crear_categoria_service(
    db,
    data
):

    return crear_categoria(
        db,
        data
    )


def obtener_categorias_service(db):

    return obtener_categorias(db)