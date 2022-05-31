# e059.py

def soma(*args):
    num = 0 
    for valorgigitado in args:
        num += valorgigitado
    print(f'O resultado da soma é {num}')

soma = soma(18,43,99,1)
