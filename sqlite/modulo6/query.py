import sqlite3

con = sqlite3.connect('modulo06.sqlite')
cur = con.cursor()

cur.execute("Select * from cidades;")
resultado = cur.fetchall()
# print(f'\n Os registros da tabela cidade é: {resultado}')

# print(type(resultado))

for x, y in resultado:
    print(f'{x}:{y}')

cur.execute("Select * from pessoas;")
todos = cur.fetchall()

for x, y, z, w, r, o, p in todos:
    print(f'{x}:{y}:{z}:{w}:{r}:{o}:{p}')
