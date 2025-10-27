# Teclea en la terminal uvicorn 01_metodos_GET.03_tipos_de_datos:app --reload

from fastapi import FastAPI

# Creamos la instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")
def leer_raiz():
    return {"mensaje" : "Vamos a ver los tipos de datos"}

@app.get("/datos")
def ver_datos():
    return 