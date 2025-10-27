# Teclea en la terminal uvicorn 01_metodos_GET.04_ejemplo_completo:app -reload

from fastapi import FastAPI
from datetime import datetime

#creamos una instancia a la aplicación FasAPI
app = FastAPI()

app.get("/fechas-mostrar")
def mostrar_datos():
    return { "fechas" : "Mostrar fechas"
    }