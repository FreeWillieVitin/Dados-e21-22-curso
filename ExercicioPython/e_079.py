#e_079.py
#Escreva um programa que recebe do usuário um número de 0 a 100 e transcreve o mesmo por extenso.
from num2words import num2words

numero = int( input('Digite um número: ') )


if numero <= 100 and numero >= 0:
    num = num2words(numero, lang='pt-br')
    print(f'Número: {num}')
else:
    print(f'Numero Invalido')
