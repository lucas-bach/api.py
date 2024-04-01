from pydantic import BaseModel
import sqlite3

class Cadastro(BaseModel):
    name: str
    phone: str
    cpf: str
    sexo: str
    state: str
    namestate: str
    city: str

def pesquisar_por_estado(cadastros, estado, limite = 10):
    resultados = []
    encontrados = 0
    
    for cadastro in cadastros:
        if cadastro["state"] == estado:
            resultados.append(cadastro)
            encontrados += 1
            
            if encontrados == limite:
                break
    
    return resultados


def pesquisar_por_sexo(cadastros, sexo, limite = 10):
    resultados = []
    encontrados = 0
    
    for cadastro in cadastros:
        if cadastro["sexo"] == sexo:
            resultados.append(cadastro)
            encontrados += 1
            
            if encontrados == limite:
                break
    
    return resultados

#colocar como função
def ler_csv():
    with open("lista.csv", 'r') as file:
        linhas = file.readlines()

    cadastros = []

    for linha in linhas[1:]:
        campos = linha.strip().split(",")
        
        state = campos[4].strip('()').replace("'", "")
        namestate = campos[5].strip('()').replace("'", "").replace(" ", "")
        
        cadastro = {
            "name": campos[0],
            "phone": campos[1],
            "cpf": campos[2],
            "sexo": campos[3],
            "state": state,
            "namestate": namestate,
            "city": campos[6],
        }
        
        cadastros.append(cadastro)
    return cadastros


def inserir_cadastro(nome):
    conn = sqlite3.connect("testnovo.db")
    cursor = conn.cursor()
    query = f"INSERT INTO pessoa (nome) VALUES (?);"
    cursor.execute(query,(nome,))
    conn.commit()
    conn.close()
















