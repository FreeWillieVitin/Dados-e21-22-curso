# 55. Crie uma função com dois parametros relacionados ao nome
#  e sobrenome de uma pessoa. A função deve retornar uma 
#  mensagem de boas vindas e esses dados devem ser digitados
#  pelo usuario. 
# 

def boas_vindas(nome,sobrenome):
    print(f'Seja bem vindo: {nome} {sobrenome}')

nome = input('Digite nome:')
sobrenome = input('Digite sobrenome:')

pessoa = boas_vindas(nome,sobrenome)




