#compreensao_list.py

lista = list([1,3,6,9,10,12,15,2,4,5])

nova_lista = [x for x in lista if x > 5]

print(nova_lista)

m = [[j for j in range(3)] for i in range(4)]
print(m)