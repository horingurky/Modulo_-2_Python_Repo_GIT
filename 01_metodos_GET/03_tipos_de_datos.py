# Teclea en la terminal uvicorn 01_metodos_GET.03_tipos_de_datos:app --reload

from fastapi import FastAPI

# Creamos la instancia de la aplicación FastAPI
app = FastAPI()

@app.get("/")
def leer_raiz():
    return {"mensaje" : "Vamos a ver los tipos de datos"}

@app.get("/datos")
def ver_datos():
    return {
        "texto" : "Hola Bingueros",
        "numero_entero" : 385,
        "numero_decimal" : 89.85432,
        "booleano" : True,
        "lista_numeros" : [275, 653, 4567, 9765],
        "lista_textos" : ["Los del Rio", "Titanblus", "Eletropork"],
        "lista_de_nooleanos" : [True, False, True],
        "Listas_misras" : 
    }