from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.schemas.producto import ProductoCreate
from app.schemas.producto import ProductoResponse

from app.services.producto_service import crear_producto_service
from app.services.producto_service import obtener_productos_service


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.post(
    "/",
    response_model=ProductoResponse
)
def crear_producto(
    data: ProductoCreate,
    db: Session = Depends(get_db)
):

    return crear_producto_service(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[ProductoResponse]
)
def listar_productos(
    db: Session = Depends(get_db)
):

    return obtener_productos_service(db)