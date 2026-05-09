from pydantic import BaseModel


class ProductoCreate(BaseModel):

    codigo_barras: str | None = None

    nombre: str

    descripcion: str | None = None

    marca: str | None = None

    precio_compra: float = 0

    precio_venta: float

    stock: float = 0

    stock_minimo: float = 0

    unidad_medida: str = "Unidad"

    iva: float = 21

    categoria_id: int | None = None


class ProductoResponse(BaseModel):

    id: int

    codigo_barras: str | None = None

    nombre: str

    descripcion: str | None = None

    marca: str | None = None

    precio_compra: float

    precio_venta: float

    stock: float

    stock_minimo: float

    unidad_medida: str

    iva: float

    activo: bool

    categoria_id: int | None = None

    class Config:

        from_attributes = True