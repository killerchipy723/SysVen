from app.repositories.producto_repository import crear_producto
from app.repositories.producto_repository import obtener_productos


def crear_producto_service(
    db,
    data
):

    return crear_producto(
        db,
        data
    )


def obtener_productos_service(db):

    return obtener_productos(db)