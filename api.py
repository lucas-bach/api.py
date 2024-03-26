from fastapi import FastAPI, Query
import uvicorn
from typing import Union
from cadastro import cadastros, pesquisar_por_estado, pesquisar_por_sexo
from typing import List


app = FastAPI()


@app.get("/")
def home():    
    return {"Listagem": len(cadastros) }


@app.get("/lista/{lista_id}")
def pegar_item(lista_id:int):
    if lista_id in cadastros:
        return cadastros[lista_id]
    else:
        return{"Erro":"verifique o ID"}

@app.get("/pesquisar/estado")
def pesquisar_estado(estado: str = Query(..., description="Estado a ser pesquisado")):
    resultado = pesquisar_por_estado(cadastros, estado)
    return {"resultados": resultado}

@app.get("/pesquisar/sexo")
def pesquisar_sexo(sexo: str = Query(..., description="Sexo a ser pesquisado")):
    resultado = pesquisar_por_sexo(cadastros, sexo)
    return {"resultados": resultado}   