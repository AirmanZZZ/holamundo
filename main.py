from typing import Optional
from fastapi import FastAPI
import json, os

app = FastAPI()

fichero_destino = "demofile.txt"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/listar")
def listar():
    f = open("demofile.txt", "r")
    return f.read()
    

@app.post("/alta/{nombre}/{telefono}")
def dar_alta(nombre: str, telefono: str):
    f = open("demofile.txt", "w")
    # {
    # "nombre": "pepe",
    # "telefono": "5551234"
    # }

    agenda = {}
    with open(fichero_destino, "r") as json_file:
        if os.stat(fichero_destino).st_size != 0:
            agenda = json.load(json_file)


    with open(fichero_destino, "w") as json_file:
        agenda[nombre] = telefono
        json.dump(agenda, json_file, indent=4)

    """
    f.write("{\"nombre\":\"" + nombre + "\",\"telefono\":\"" + telefono + "\"}")
    f.close()
    """
    return ["alta realizada correctamente"]

