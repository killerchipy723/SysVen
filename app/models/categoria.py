# app/models/categoria.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.core.database import Base


class Categoria(Base):

    __tablename__ = "categorias"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )

    descripcion = Column(
        String(255),
        nullable=True
    )

    activo = Column(
        Boolean,
        default=True
    )

    def __repr__(self):

        return f"<Categoria {self.nombre}>"