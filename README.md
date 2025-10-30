# Modulo_-2_Python_Repo_GIT
Curso Python modulo 2 FastAPI


Crear entorno virtual en Visual Studio Code
1.    Borras la carpeta .venv
 
2 Crear un nuevo entorno virtual
En la terminal integrada de VS Code:
python -m venv .venv
Esto creará una nueva carpeta .venv dentro del proyecto.

3 Activar el nuevo entorno
Luego actívalo:
.\.venv\Scripts\activate

4 Instalar dependencias 
 instálalas con:
pip install -r requirements.txt

💡 5️⃣ (Opcional) Configurar VS Code para usar el nuevo entorno

Pulsa     Ctrl + Shift + P 
Escribe     “Python: Select Interpreter” 
Elige     el que diga algo como: 
.venv\Scripts\python.exe
Así VS Code usará ese entorno para ejecutar y depurar tu código.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# modelo básico
class Usuario(BaseModel):
    nombre: str
    edad: int
    activo: bool

# modelo con campos opcionales y valores por defecto
class Producto(BaseModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    disponible: bool = True

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": f"Usuario {usuario.nombre} creado correctamente"
    }

@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "producto_creado": producto.nombre,
        "precio": producto.precio,
        "disponible": producto.disponible
    }


