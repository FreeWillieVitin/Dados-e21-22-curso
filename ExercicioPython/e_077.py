#e_077.py
#Defina uma função que pode aceitar duas string como entrada,
#exibindo em tela apenas a string de maior tamanho/comprimento. Caso as duas string tenham mesmo tamanho exiba as duas.
def valor(a,b):
    if (a > b):
        print(f'{a}')
    else:
        print(f'{b}')

teste = input('Digite um valor: ')
teste2 = input('Digite um valor: ')

resultado = valor(teste,teste2)