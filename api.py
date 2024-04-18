from fastapi import FastAPI, Query
import uvicorn
from typing import Union
from cadastro import insert_users, ler_csv, ler_ultimo_cadastro, consultar_por_nome,alterar_cadastro,deletar_cadastro
from typing import List
from models import CreatePessoa



app = FastAPI()                                                        


@app.get("/query_10")
def home():
    dados_cvs = ler_csv()    
    return  dados_cvs[:10]


@app.get("/query_by_name/{name}")
def consulte(name: str) -> CreatePessoa:
         
    return consultar_por_nome(name)

@app.get("/query_by_id/{id}")
def consulte(name: str) -> CreatePessoa:
         
    return consultar_por_nome(name)


@app.post("/create_cad")
def create(pessoa : CreatePessoa):
    insert_users(pessoa)
      
    return ler_ultimo_cadastro() 


@app.put("/create_cad")
def create(pessoa : CreatePessoa):
    insert_users(pessoa)
      
    return ler_ultimo_cadastro() 



@app.patch("/edit_name/{id}/{new_name}/{new_phone}/{new_sexo}/{new_state}/{new_namestate}/{new_city}")
def edit_name(id: int, new_name: str, new_phone: str = "", new_sexo: str = "", new_state: str = "", new_namestate: str = "", new_city: str = ""):
    alterar_cadastro(id, new_name, new_phone, new_sexo, new_state, new_namestate, new_city)
    return {"message": "Nome alterado com sucesso"}



@app.delete("/{id}")
def del_cad(id):
    deletar_cadastro(id)    
    return {"message": "Cadastro deletado"} 




if __name__=="__main__":
    uvicorn.run(app)






