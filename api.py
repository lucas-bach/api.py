from fastapi import FastAPI
import uvicorn
from typing import Union
from cadastro import cadastros




app = FastAPI()

# cadastros = {
    
#     1:{"nome": "Isadora Melo", "fone": "+55 84 7602 1091,624.750.381-44", "sexo": "M", "state": ("RR", "Roraima"), "city": "Cardoso"},
#     2:{"nome": "Augusto Dias", "fone": "(041) 4955-5356,296.851.370-21", "sexo": "F", "state": ("SC", "Santa Catarina"), "city": "Barbosa de Novaes"},
#     3:{"nome": "Srta. Marcela Fernandes", "fone": "+55 (051) 2751-0516,849.125.730-60", "sexo": "F", "state": ("SC", "Santa Catarina"), "city": "Barbosa do Amparo"},
#     4:{"nome": "Cauã Viana", "fone": "+55 (011) 1438-9943,425.361.097-80", "sexo": "F", "state": ("RN", "Rio Grande do Norte"), "city": "da Cunha Alegre"},
#     5:{"nome": "Sra. Camila Cardoso", "fone": "+55 (061) 2434 7123,847.593.126-09", "sexo": "F", "state": ("AL", "Alagoas"), "city": "Nunes"},
#     6:{"nome": "Yuri Castro", "fone": "+55 (051) 2768 1713,895.074.312-41", "sexo": "M", "state": ("TO", "Tocantins"), "city": "Carvalho Grande"},
#     7:{"nome": "Cecília da Rosa", "fone": "51 2708 8995,196.570.482-49", "sexo": "F", "state": ("RR", "Roraima"), "city": "Azevedo"},
#     8:{"nome": "Sr. Calebe Oliveira", "fone": "(061) 0437 8091,496.572.180-20", "sexo": "M", "state": ("PE", "Pernambuco"), "city": "Pires"},
#     9:{"nome": "Ana Sophia Castro", "fone": "71 2037 5968,378.961.250-21", "sexo": "F", "state": ("SP", "São Paulo"), "city": "Ferreira dos Dourados"}

# }

cadastros = []



@app.get("/")
def home():    
    return {"Listagem": len(cadastros) }


@app.get("/lista/{lista_id}")
def pegar_item(lista_id:int):
    if lista_id in cadastros:
        return cadastros[lista_id]
    else:
        return{"Erro":"verifique o ID"}