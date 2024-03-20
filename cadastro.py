# file = open("lista.csv",'r')

# cadastros = []
# n = 0

# while True:
#     line =  file.readline() 
#     if not line or n > 1000:
#         break
#     cadastros.append(line)
#     n += 1


# for i,cadastro in enumerate(cadastros):
#     linha_cadastro = cadastro.split(",")
#     print(cadastro)
#     print(i)


with open("lista.csv", 'r') as file:
    linhas = file.readlines()


cadastros = []


for linha in linhas[1:]:    
    campos = linha.strip().split(",")

    state = campos[4].strip('()')
    namestate = campos[5].strip('()')
    
    cadastro = {
        "name": campos[0],
        "phone": campos[1],
        "cpf": campos[2],
        "sexo": campos[3],
        "state": state,
        "namestate": namestate,
        "city": campos[6]
    }
    
    cadastros.append(cadastro)


for i, cadastro in enumerate(cadastros[:1]):
    print(f"Cadastro {i+1}: {cadastro}")