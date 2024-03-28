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

# CREATE TABLE Clientes (
#     idCliente INTEGER      PRIMARY KEY AUTOINCREMENT,
#     nome      VARCHAR (70) NOT NULL
# );

# CREATE TABLE ContasReceber (
#     fatura     INTEGER,
#     parcela    INTEGER,
#     idCliente  INTEGER         NOT NULL,
#     valor      DECIMAL (18, 2) NOT NULL,
#     vencimento DATE            NOT NULL,
#     DataBaixa  DATE
# );




# Inserindo dados na tabela
#cursor.execute("INSERT INTO pessoa (ID,nome) VALUES (?,?)",(2,'Maria',))
# pessoas = cursor.execute("SELECT * FROM pessoa")
# print(pessoas.fetchall())



# Salvando as alterações
conn.commit()