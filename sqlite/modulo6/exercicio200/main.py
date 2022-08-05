from random import randint
import sqlite3
import pandas as pd

con = sqlite3.connect('exercicio.sqlite')
cur = con.cursor()

city = pd.read_csv('C:\\Users\\Victor\\Desktop\\idad.csv', delimiter=',')
city.head()
nome = pd.read_csv('C:\\Users\\Victor\\Desktop\\nomes.csv', delimiter=',')


cur.execute("""     
drop TABLE IF EXISTS cidades;
""")

cur.execute("""
create table CIDADES (
    id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
    uf varchar(10) NOT NULL,
    nome_cidade varchar(50) NOT NULL
);
""")

cur.execute("""     
drop TABLE IF EXISTS pessoas;
""")

cur.execute("""
CREATE TABLE PESSOAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME     varchar(50) NOT NULL,
    IDADE    INTEGER ,
    ID_CIDADE VARCHAR(30)   
);
""")

city.to_sql("CIDADES", con, if_exists='append', index=False)

n_cidades = (len(city))

nomes = pd.read_csv('C:\\Users\\Victor\\Desktop\\nomes.csv', sep=',')
nome = nomes['NOME']
for n in nome:
    idade = randint(0, 100)
    cidade = randint(1, n_cidades)
    cur.execute("""
        INSERT INTO PESSOAS
            (NOME, IDADE, ID_CIDADE) 
                VALUES
            ('{}', '{}', '{}');""".format(n.upper(), idade, cidade))

con.commit()


# cur.execute("Select * from CIDADES;")
# resultado = cur.fetchall()
# print(f'\n Os registros da tabela cidade é: {resultado}\n')

# cur.execute("SELECT COUNT(ID_CIDADE) FROM CIDADES")
# total = cur.fetchall()
# print(f'\n A quantidade de registros na tabela é de: {total}\n')

# cur.execute("Select * from PESSOAS;")
# resultado = cur.fetchall()
# print(f'\n Os registros da tabela pessoas é: {resultado}\n')

# cur.execute("SELECT COUNT(ID) FROM PESSOAS")
# total = cur.fetchall()
# print(f'\n A quantidade de registros na tabela é de: {total}\n')

cur.execute("Select A.NOME, A.IDADE, B.NOME_CIDADE, B.UF FROM PESSOAS AS A, CIDADES AS B ORDER BY B.UF, B.NOME_CIDADE, A.NOME, A.IDADE;")
resultado = cur.fetchmany(2)
print(resultado)