#e_086.py
"""
A partir de uma lista composta apenas de dados numéricos, gere outra
lista usando list comprehension usando como base a lista anterior, 
compondo a nova com valores dos elementos originais elevados ao cubo.
Dado que lista = [1,2,3,4,5,6].
"""

lista = [1,2,3,4,5,6]
lista_cubos = [numero ** 3 for numero in lista]
print(lista_cubos)