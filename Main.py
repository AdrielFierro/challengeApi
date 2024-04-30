from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Optional
import json
app = FastAPI()

class Libro(BaseModel):
    id: Optional[int] = None
    nombre:str
    autor: str
    categoria: str
    resumen: str

with open('libros.json','r') as f:
    libros= json.load(f)['libros']



@app.get("/libros")
def todos():
    return libros


@app.get('/libros/{l_id}')
def get_libros(l_id:int):
    libro= [l for l in libros if l['id'] == l_id]
    return libro[0] if len(libro) > 0 else {"No existe un libro con ese id"} 


@app.get("/buscar")
def buscar_categoria(categoria: str = Query(None, title="categoria", description="buscar por categoria categoria")):
    libro = [l for l in libros if l['categoria'] == categoria]
    return libro


@app.post('/addlibros')
def añadir_libro(libro: Libro):
    l_id= max([l['id'] for l in libros]) + 1 
    new_libro = {
"id": l_id,
"nombre": libro.nombre,
"autor": libro.autor,
"categoria": libro.categoria,
"resumen":libro.resumen

    }
    libros.append(new_libro)

    with open('libros.json','w') as f:
        json.dump(libros,f)
    return new_libro

# @app.delete("/libros")
# def eliminar_libro():
#     return print("wip")




