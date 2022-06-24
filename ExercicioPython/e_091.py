# e_091.py
# Escreva um programa da forma mais reduzida possível, que recebe do usuario uma série de nomes,
# separando os mesmos e os organizando em ordem alfabetica. Em Seguida exiba em tela os nomes já ordenados.

my_list = [x for x in input('digites os nomes separados por virgula').split(',')]
my_list.sort()
print(','.join(my_list))