import sqlite3  # Importa o sqlite3

con = sqlite3.connect('modulo06.sqlite')  # Cria ou conecta um(em um) banco de dados
cur = con.cursor()  # Define a variavel que vai trabalhar com o banco


#  .execute é o metodo usado para executar comandos sql atraves de um arquivo python
#  apos o .execute é inserido a query dentro de aspas duplas como se fosse uma doc string e parenteses
cur.execute("""     
drop TABLE IF EXISTS cidades;
""")

cur.execute("""
create table cidades (
    id_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
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

cur.execute("""
INSERT INTO cidades (nome_cidade)
    VALUES ('Mafra'),
    ('Rio Negro'),
    ('Curitiba'),
    ('São Bento do Sul');
""")

cur.execute("""
INSERT INTO pessoas (CPF, NOME, IDADE, ENDERECO, SALARIO, ID_CIDADE)
    VALUES ('111.318.679-80', 'Victor Hugo', 24, 'Rua das flores', 1300.00, 1),
    ('333.444.555-90', 'Marieli Stankievski', 23, 'Rua das flores', 1300.00, 4),
    ('111.318.679-80', 'Jorge', 68, 'Rua das flores', 1300.00, 3),    
    ('111.318.679-80', 'James', 25, 'Rua das flores', 1300.00, 2);
""")


#  con.commit() pode ser feito o commit dessa forma ou atraves de query commit usando o .execute

cur.execute("""
commit
""")

#  Fetchone() retorna o primeiro resultado
cur.execute("Select * from cidades;")
resultado = cur.fetchone()
print(f'\n O primeiro resultado é: {resultado}')

#  Fetchmany(2) retorna a quantidade de resultados solicitados por parametro
cur.execute("Select * from cidades;")
resultado = cur.fetchmany(2)
print(f'\n As duas primeiras linhas são: {resultado}')

#  Fetchall() retorna todos os resultados
cur.execute("Select * from cidades;")
resultado = cur.fetchall()
print(f'\n Os registros da tabela cidade é: {resultado}')

