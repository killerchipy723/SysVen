from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.schemas.auth import LoginSchema

from app.core.dependencies import get_db

from app.services.auth_service import login_usuario

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):

    resultado = login_usuario(
        db,
        data.usuario,
        data.password
    )

    if not resultado:

        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )

    return resultado