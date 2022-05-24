# e060.py

def id(*args,**kwargs):
    for n in args:
        nome = n
        print(f'{n}')
    
        for k,v in kwargs.items():
            idade = k
            sexo = v
            print(f'{idade},{sexo}')

            print(f'Nome:{nome},{idade},{sexo}')

id('Victor', idade=24,sexo='M')
