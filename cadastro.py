from pydantic import BaseModel
import sqlite3
from models import CreatePessoa,UpdatePessoa


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


def insert_users(pessoa : CreatePessoa):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "INSERT INTO dadosusuarios (name,phone,cpf,sexo,state,namestate,city) VALUES (?,?,?,?,?,?,?);"   
    cursor.execute(query,(pessoa.name,pessoa.phone,pessoa.cpf,pessoa.sexo,pessoa.state,pessoa.namestate,pessoa.city))
    conn.commit() 
    conn.close() 


def ler_ultimo_cadastro():
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "SELECT * FROM dadosusuarios ORDER BY ROWID DESC LIMIT 1;"
    cursor.execute(query)
    ultimo_cadastro = cursor.fetchone()
    conn.close()

    if ultimo_cadastro:
        return ultimo_cadastro  
    else:
        return []    


def consultar_por_nome(name: str) -> CreatePessoa:
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "SELECT * FROM dadosusuarios WHERE name = ?;"
    cursor.execute(query, (name,))
    resultados = cursor.fetchone()
    conn.close()

    if resultados:        
        return CreatePessoa(name=resultados[1], phone=resultados[2], sexo=resultados[3], state=resultados[4], namestate=resultados[5], city=resultados[6])
    else:
        return "Nenhum cadastro"  


def consultar_por_id(id: str ) -> CreatePessoa:
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "SELECT * FROM dadosusuarios WHERE id = ?;"
    cursor.execute(query, (id,))
    consulte = cursor.fetchone()
    conn.close()

    if consulte:
        return CreatePessoa(id=[0])
    else:
        return "Esse id não existe!"
    


def alterar_cadastro(id: int, pessoa : CreatePessoa):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "UPDATE dadosusuarios SET name = ?, phone = ?, sexo = ?, state = ?, namestate = ?, city = ? WHERE id = ?;"
    cursor.execute(query, (pessoa.name,pessoa.phone,pessoa.sexo,pessoa.state,pessoa.namestate,pessoa.city, id))

    conn.commit()
    conn.close()


def alterar_parcial_cadastro(id: int, pessoa : UpdatePessoa ):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    filters = []
    variables = []

    if pessoa.name is not None:
       filters.append(f"name= ?")
       variables.append(pessoa.name)

    if pessoa.phone is not None:
       filters.append("phone=?")
       variables.append(pessoa.phone)

    if pessoa.phone is not None:
       filters.append("sexo=?")
       variables.append(pessoa.sexo)

    if pessoa.phone is not None:
       filters.append("state=?")
       variables.append(pessoa.state)

    if pessoa.phone is not None:
       filters.append("namestate=?")
       variables.append(pessoa.namestate)

    if pessoa.phone is not None:
       filters.append("city=?")
       variables.append(pessoa.city)      


    variables.append(id) 
      
    filters_set = ",".join(filters)    

    query = f"UPDATE dadosusuarios SET {filters_set}  WHERE id = ?;"
    cursor.execute(query, variables)        

    conn.commit()
    conn.close()
    

def deletar_cadastro(id):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "DELETE FROM dadosusuarios WHERE id = ?;"
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()






   

    




# def inserir_cadastro(nome):
#     conn = sqlite3.connect("register.db")
#     cursor = conn.cursor()
#     query = "INSERT INTO pessoa (nome) VALUES (?);"
#     cursor.execute(query,(nome,))
#     conn.commit()
#     conn.close()

# def delete_cadastro(nome):
#     conn = sqlite3.connect("register.db")
#     cursor = conn.cursor()
#     query = "DELETE FROM pessoa WHERE nome = (?);"
#     cursor.execute(query,(nome,))
#     conn.commit()
#     conn.close()    

# def atualizar_cadastro(nome_antigo, nome_novo):
#     conn = sqlite3.connect("register.db")    
#     cursor = conn.cursor()
#     query = "UPDATE pessoa SET nome = (?) WHERE nome = (?);"
#     cursor.execute(query, ( nome_novo, nome_antigo))
#     conn.commit()
#     conn.close()

# def ler_cadastro(nome):
#     conn = sqlite3.connect("register.db")
#     cursor = conn.cursor()
#     query = "SELECT * FROM pessoa WHERE nome = ?;"
#     cursor.execute(query, (nome,))
#     resultado = cursor.fetchone()
#     conn.close()
#     return resultado

    
    













