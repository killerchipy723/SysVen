from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

import os

# Cargar variables .env
load_dotenv()

# Obtener URL conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear engine SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Crear sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos
Base = declarative_base()