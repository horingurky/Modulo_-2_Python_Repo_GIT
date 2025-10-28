"""
Los query parameters (parametros de consulta) son clave-valor que se utilizan para filtrar, ordenar y paginar.

Se añadeb despues de la ruta con un signo de interrogación de cierre ? y se separan
 con un ampersam "&".
"""

from fastapi import FastAPI

app = FastAPI()

# Paginación simple
app.get("/users")
def get_users(limit : int 10):
    return {
        "users" [f"Usuario{i}" for i in range(1, limit+1)],
        "total" limit,
        "limit" limit
    }

# Paginación completa
app.get("/products")
def get_products(limit : int = 0, skip : int = 0):
    products = [f"Producto {i}" for i in range(skip+1,skip + limit +1)]
    return {
        "Productos" : products,
        "limit" : limit,
        "skip" : skip,
        "total_show" : len(products)
    }

app.get("/items")
def get_items(category : str = "all")



