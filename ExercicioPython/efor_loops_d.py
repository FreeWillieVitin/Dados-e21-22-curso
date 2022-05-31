#efor_loops_d.py

l_d_l = [ [1,2,3],['a','b','c'],['@','$','%']]

for x in l_d_l:
    for y in x:
            print(y, end=' ')
print()

lista_caixa = [ [10,20,30],[15,1,2],[50,3,5], [45,12,7], [100,200,300]]
volume_total = 0
for a, b, c in lista_caixa:
    print(a, b, c," volume é:", (a*b*c))
    volume_total += (a*b*c)
#Agora multiplicar
p0=1
p1=1
p2=1
lista = [ [10,20,30],[15,1,2],[50,3,5], [45,12,7], [100,200,300]] 
for x in lista:
    print(x)
    p0 *= x[0]
    p1 *= x[1]
    p2 *= x[2]

    print(p0,p1,p2)




    