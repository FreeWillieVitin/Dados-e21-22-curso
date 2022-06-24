#e_092.py
"""
 Escreva um simples programa que recebe do usuário um número qualquer, retornando ao mesmo se este número é um numero perfeito.
 '''Um número se diz perfeito se é igual à soma de seus divisores próprios.
 Divisores próprios de um número positivo N são todos os divisores inteiros positivos de N exceto o próprio N.
 Por exemplo, o número 6, seus divisores próprios são 1, 2 e 3, cuja soma é igual à 6.
 1 + 2 + 3 = 6

"""
n = int(input("Digite um número:"))
cont = 1
soma = 0

while cont<n:
 if n%cont==0:
     soma = soma + cont
     cont = cont + 1
 else:
     cont = cont + 1
     
     
if soma==n:
    print ("perfeito")
else:
    print("nao prefeito")