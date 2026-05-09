from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.schemas.categoria import CategoriaCreate
from app.schemas.categoria import CategoriaResponse

from app.services.categoria_service import crear_categoria_service
from app.services.categoria_service import obtener_categorias_service


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


@router.post(
    "/",
    response_model=CategoriaResponse
)
def crear_categoria(
    data: CategoriaCreate,
    db: Session = Depends(get_db)
):

    return crear_categoria_service(
        db,
        data
    )


@router.get(
    "/",
    response_model=list[CategoriaResponse]
)
def listar_categorias(
    db: Session = Depends(get_db)
):

    return obtener_categorias_service(db)