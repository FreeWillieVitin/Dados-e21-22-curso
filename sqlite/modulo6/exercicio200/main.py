import sqlite3
import pandas as pd

con = sqlite3.connect('exercicio.sqlite')
cur = con.cursor()

city = pd.read_csv('C:\\Users\\Victor\\Desktop\\idad.csv', delimiter=',')
city.head()

cur.execute("""     
drop TABLE IF EXISTS cidades;
""")

cur.execute("""
create table cidades (
    id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
    uf varchar(10) NOT NULL,
    nome_cidade varchar(50) NOT NULL
);
""")

cur.execute("""     
drop TABLE IF EXISTS pessoas;
""")

cur.execute("""
CREATE TABLE pessoas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CPF      varchar(14) NOT NULL,
    NOME     varchar(50) NOT NULL,
    IDADE    INTEGER     NOT NULL,
    ENDERECO    VARCHAR(50),
    SALARIO     REAL,
    ID_CIDADE VARCHAR(30)   
);
""")


city.to_sql("cidades", con, if_exists='append', index=False)

cur.execute("Select * from cidades;")
resultado = cur.fetchall()
print(f'\n Os registros da tabela cidade é: {resultado}')

cur.execute("Select seq from sqlite_sequence;")
total = cur.fetchall()
print(f'\n A quantidade de registros na tabela é de: {total}')