from pydantic import BaseModel
import sqlite3
from models import CreatePessoa


# def pesquisar_por_estado(cadastros, estado, limite = 10):
#     resultados = []
#     encontrados = 0
    
#     for cadastro in cadastros:
#         if cadastro["state"] == estado:
#             resultados.append(cadastro)
#             encontrados += 1
            
#             if encontrados == limite:
#                 break
    
#     return resultados


# def pesquisar_por_sexo(cadastros, sexo, limite = 10):
#     resultados = []
#     encontrados = 0
    
#     for cadastro in cadastros:
#         if cadastro["sexo"] == sexo:
#             resultados.append(cadastro)
#             encontrados += 1
            
#             if encontrados == limite:
#                 break
    
#     return resultados


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
    resultados = cursor.fetchall()
    conn.close()  
    return CreatePessoa(name=resultados[0],phone=resultados[1])


def alterar_cadastro(id, new_name, new_phone, new_sexo, new_state, new_namestate, new_city):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    if new_name != "":
        query = "UPDATE dadosusuarios SET name = ? WHERE id = ?;"
        cursor.execute(query, (new_name,id))
    elif new_phone != "":
        query = "UPDATE dadosusuarios SET phone = ? WHERE id = ?;"
        cursor.execute(query, (new_phone,id))

    conn.commit()
    conn.close()


def deletar_cadastro(id):
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    query = "DELETE FROM dadosusuarios WHERE id = ?;"
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()




# def alterar_cadastro(id, name, phone, cpf, sexo, state, namestate, city):
#     conn = sqlite3.connect("register.db")
#     cursor = conn.cursor()
#     query = "UPDATE dadosusuarios SET name = ?, phone = ?, cpf = ?, sexo = ?, state = ?, namestate = ?, city = ? WHERE id = ? AND name = ?"
#     cursor.execute(query, (name, phone, cpf, sexo, state, namestate, city, id ,name))
#     conn.commit()
#     conn.close()

# def alterar_cadastro(id, name, phone, cpf, sexo, state, namestate, city):
#     conn = sqlite3.connect("register.db")
#     cursor = conn.cursor()
#     query = "UPDATE dadosusuarios SET name=?, phone=?, cpf=?, sexo=?, state=?, namestate=?, city=? WHERE id=? AND name=?;"
#     cursor.execute(query, (name, phone, cpf, sexo, state, namestate, city, id, name))
#     conn.commit()
#     conn.close()

# # Exemplo de uso:
# alterar_cadastro(1, "Novo Nome", "Novo Telefone", "Novo CPF", "Novo Sexo", "Novo Estado", "Nova Cidade", "Novo Estado", "Nova Cidade")


   

    




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
#     conn = sqlite3.connect("register.db")#     cursor = conn.cursor()
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

    
    













