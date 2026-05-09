from app.models.producto import Producto


def crear_producto(
    db,
    data
):

    producto = Producto(
        codigo_barras=data.codigo_barras,
        nombre=data.nombre,
        descripcion=data.descripcion,
        marca=data.marca,
        precio_compra=data.precio_compra,
        precio_venta=data.precio_venta,
        stock=data.stock,
        stock_minimo=data.stock_minimo,
        unidad_medida=data.unidad_medida,
        iva=data.iva,
        categoria_id=data.categoria_id
    )

    db.add(producto)

    db.commit()

    db.refresh(producto)

    return producto


def obtener_productos(db):

    return db.query(Producto).all()