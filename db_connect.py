import sqlite3
conn = sqlite3.connect("financeiro.db")

# Criando um cursor
cursor = conn.cursor()

# Criando uma tabela
# cursor.execute('''CREATE TABLE pessoa (
#     id INTEGER PRIMARY KEY ,
#     nome TEXT
# );
# ''')


# Inserindo dados na tabela
#cursor.execute("INSERT INTO pessoa (ID,nome) VALUES (?,?)",(2,'Maria',))
# pessoas = cursor.execute("SELECT * FROM pessoa")
# print(pessoas.fetchall())



# Salvando as alterações
conn.commit()