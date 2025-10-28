
# Teclea en consola uvicorn 01_metodos_GET.Reto_FastAPI_zoologico:app --reload

from fastapi import FastAPI
from datetime import datetime

# Creamos una instancia a una aplicación FastAPI
app = FastAPI()

@app.get("/animales")
def mostrar_animales():
    return {"animales" : ["León", "Rinoceronte", "Delfin", "Ballena"]}

@app.get("/zoologico")
def info_zoologico():
    return {
        "nombre" : "ZOOTROL",
        "cantidad de animales" : 486,
        "abierto" : True,
        "horario" : "de 9 a 21 horas"
    }

@app.get("/estadisticas")
def mostrar_estadisticas():
    return {
        "informacion_general":{
            "nombre": "ZOOTROL",
            "ubicacion" : "Chorrilandia"
        },
        "datos_de_animales" :{
            "total_especies" : 4,
            "animales_populares" : ["Rinoceronte", "Delfín"]
        },
        "estado_operacional" : {
            "abierto" : True,
            "empleados" : 43
        }
    }
