from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.core.database import Base

import uuid


class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    usuario = Column(
        String(50),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    activo = Column(
        Boolean,
        default=True
    )

    rol_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    rol = relationship("Rol")