#e_080.py
from posixpath import split


#split é uma função utilizada para a manipulação de strings
#Ele permite dividir o conteudo da variavel de acordo com as 
#condiçoes especificadas em cada parametro da função ou com os valores predefinidos por padrao
nome = input('Digite seu nome e sobrenome: ')
n = nome.split()
print(f'Seu nome é: {n[-1]} {n[0]}')