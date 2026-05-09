from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine
from app.core.database import Base

from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.categoria import Categoria
from app.models.producto import Producto

from app.routers.auth import router as auth_router
from app.routers.categoria import router as categoria_router
from app.routers.producto import router as producto_router


# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SysVen API"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)
app.include_router(categoria_router)
app.include_router(producto_router)


@app.get("/")
def home():

    return {
        "message": "SysVen funcionando correctamente"
    }