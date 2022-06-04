#e_073.py
#Escreva um programa que encontre todos os números que são divisiveis por 7, mas que não são multiplos de 5, entre 200 e 2200 (ambos incluidos).
#Os números obtidos devem ser impressos em sequencia, separados por virgula e em uma unica linha. (5)
lista = []
for i in range (200,2200):
    if i % 7 == 0:
        if i % 5 != 0:
            print('{}'.format(i), end=' ')