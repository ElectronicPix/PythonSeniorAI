from fastapi import FastAPI  # Importamos la libreria de fast API
from pydantic import BaseModel # Hacer peticiones basados en un modelo

app = FastAPI()  # Archivo se comporte como proyecto de Fast API


# Ruta de conexión
@app.get("/")
async def root():
    return {"message": "Hola Mundo"}


# Recibir información
@app.get("/usuarios/{id}")
def leer_usuario(id: int):
    return {"id": id, "nombre": "Juan"}
