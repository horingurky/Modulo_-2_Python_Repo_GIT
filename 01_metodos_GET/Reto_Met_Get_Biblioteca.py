"""
Crea una aplicación FastAPI con dos endpoints GET específicos:

Un endpoint en la ruta /libros que devuelva una respuesta JSON con una lista de 3 libros. Cada libro debe ser simplemente un string con el título.

Para empezar:

Importa FastAPI
Crea la instancia de la aplicación con app = FastAPI()
Define cada endpoint usando el decorador @app.get() seguido de la función correspondiente
Cada función debe devolver un diccionario de Python (FastAPI lo convertirá automáticamente a JSON)
Para el endpoint de biblioteca, incluye las claves: "nombre", "total_libros" (número), y "abierta" (booleano).
"""

# TECLEA EN LA TERMINAL uvicorn 01_metodos_GET.Reto_Met_Get_Biblioteca:app --reload

from fastapi import FastAPI

# Crear la instancia de la aplicación
app = FastAPI()

# Escribe aquí tu código para los endpoints GET
@app.get("/libros")
def listar_raiz():
    return {"Listado":["el señor de los anillos", "La perdición de la letanía", "Mangueras a lo loco"]}

@app.get("/biblioteca")
def biblioteca_mostrar():
    return {"nombre":"Biblioteca Rural","Total_libros": 3, "abierta": True}