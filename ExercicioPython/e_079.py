#e_079.py
#Escreva um programa que recebe do usuário um número de 0 a 100 e transcreve o mesmo por extenso.
from num2words import num2words

numero = int( input('Digite um número: ') )

num_ptbr = num2words(numero, lang='pt-br')
print(f'Número: {num_ptbr}')

num_ptbr_ord = num2words(numero, lang='pt-br', to='ordinal')
print(f'Número (ordinal): {num_ptbr_ord}')
