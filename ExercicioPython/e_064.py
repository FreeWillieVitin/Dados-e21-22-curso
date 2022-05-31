#e_062.py
numeros = (33, 1987, 2020)
dados = {'Nome':'Victor','Profissão':'Programador'}

def id(*args,**Kwargs):
    print(args)
    print(Kwargs)
    print(Kwargs,['Nome'])
    print(Kwargs,['Profissão'])

id(*numeros, **dados)