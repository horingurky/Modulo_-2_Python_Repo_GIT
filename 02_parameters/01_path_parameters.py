"""



"""
from fastapi import FastAPI

app= FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id):
    return {
        "user_id" : user_id,
        "name" : f"Usuario {user_id}",
        "email" : f"usuario{user_id}@netflix.com",
        "status" : "acrivo"
    }


