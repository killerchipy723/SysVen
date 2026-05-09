# app/models/producto.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from app.core.database import Base


class Producto(Base):

    __tablename__ = "productos"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Código barras opcional
    codigo_barras = Column(
        String(100),
        unique=True,
        nullable=True
    )

    # Nombre obligatorio
    nombre = Column(
        String(255),
        nullable=False
    )

    # Descripción opcional
    descripcion = Column(
        Text,
        nullable=True
    )

    # Marca opcional
    marca = Column(
        String(100),
        nullable=True
    )

    # Precio compra
    precio_compra = Column(
        Float,
        default=0,
        nullable=False
    )

    # Precio venta obligatorio
    precio_venta = Column(
        Float,
        default=0,
        nullable=False
    )

    # Stock actual
    stock = Column(
        Float,
        default=0,
        nullable=False
    )

    # Stock mínimo
    stock_minimo = Column(
        Float,
        default=0,
        nullable=False
    )

    # Unidad medida
    unidad_medida = Column(
        String(50),
        default="Unidad",
        nullable=False
    )

    # IVA
    iva = Column(
        Float,
        default=21,
        nullable=False
    )

    # Producto activo
    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    # FK categoría
    categoria_id = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=True
    )

    categoria = relationship("Categoria")

    def __repr__(self):

        return f"<Producto {self.nombre}>"