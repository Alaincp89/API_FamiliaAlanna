from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def saludo():
    return{"Hello": "David"}


miembros_familia_alanna = {
    1: {
        "Parentesco": "Mamá",
        "Nombre": "Vanessa",
        "Apellido": "Cortina",
        "Edad": "31"
    },
    2: {
        "Parentesco": "Papá",
        "Nombre": "Alain",
        "Apellido": "Cervantes",
        "Edad": "35"
    },
    3: {
        "Parentesco": "Tío",
        "Nombre": "David",
        "Apellido": "Cortina",
        "Edad": "28"
    },
    4: {
        "Parentesco": "Abuela",
        "Nombre": "Rut",
        "Apellido": "Fernandez",
        "Edad": "62"
    }
}

@app.get("/familia/id/{id}")
def obtener_miembro_familia(id: int):
    miembro = miembros_familia_alanna.get(id)
    if miembro:
        return{"Miembro": miembro }
    else:
        return{"Message": f"Miembro con el ID {id} de la familia no encontrado"}
    
    
class Miembro(BaseModel):
    id: int
    parentesco: str
    nombre: str
    apellido: str
    edad: int
    
    
@app.post("/familia")
def crear_miembro_familia(miembro: Miembro):
    return{"Message": f"{miembro.nombre} creado exitosamente" }    