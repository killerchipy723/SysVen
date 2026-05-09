from app.core.database import SessionLocal

from app.models.usuario import Usuario
from app.models.rol import Rol

from app.core.security import hash_password


db = SessionLocal()

# Crear rol administrador
rol_admin = Rol(
    nombre="Administrador"
)

db.add(rol_admin)

db.commit()

db.refresh(rol_admin)

# Crear usuario admin
admin = Usuario(
    nombre="Administrador",
    usuario="admin",
    password=hash_password("123456"),
    rol_id=rol_admin.id
)

db.add(admin)

db.commit()

print("Administrador creado correctamente")