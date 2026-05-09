from app.models.categoria import Categoria


def crear_categoria(
    db,
    data
):

    categoria = Categoria(
        nombre=data.nombre,
        descripcion=data.descripcion
    )

    db.add(categoria)

    db.commit()

    db.refresh(categoria)

    return categoria


def obtener_categorias(db):

    return db.query(Categoria).all()