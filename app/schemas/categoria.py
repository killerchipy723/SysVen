from pydantic import BaseModel


class CategoriaCreate(BaseModel):

    nombre: str

    descripcion: str | None = None


class CategoriaResponse(BaseModel):

    id: int

    nombre: str

    descripcion: str | None = None

    activo: bool

    class Config:

        from_attributes = True