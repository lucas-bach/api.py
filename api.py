from fastapi import FastAPI, Query
import uvicorn
from cadastro import insert_users, ler_csv, ler_ultimo_cadastro, consultar_por_nome,alterar_cadastro,deletar_cadastro,alterar_parcial_cadastro
from models import CreatePessoa, UpdatePessoa


app = FastAPI()                                                        


@app.get("/query_10")
def home():
    dados_cvs = ler_csv()    
    return  dados_cvs[:10]


@app.get("/query_by_name/{name}")
def consultar_nome(name: str) -> CreatePessoa:         
    return consultar_por_nome(name)     
   

@app.post("/create_cad")
def create(pessoa : CreatePessoa):
    insert_users(pessoa)      
    return ler_ultimo_cadastro(pessoa) 


@app.put("/update/{id}")
def to_update(id: int, pessoa : CreatePessoa):
    alterar_cadastro(id,pessoa)      
    return "Cadastro atualizado"



@app.patch("/edit_name/{id}")
def edit_name(id: int, pessoa : UpdatePessoa):
    alterar_parcial_cadastro(id, pessoa)
    return {"message": "Nome alterado com sucesso"}



@app.delete("/{id}")
def del_cad(id):
    deletar_cadastro(id)    
    return {"message": "Cadastro deletado"} 




if __name__=="__main__":
    uvicorn.run(app)






