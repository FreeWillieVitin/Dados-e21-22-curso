#e_090.py
#  Crie um programa que recebe do usuário uma sequencia de números aleatórios separados por vírgula,
#  armazene os números um a um, em formato de texto, como elementos ordenados de uma lista.
#  Mostre em tela a lista com seus respectivos elementos após serem ordenados. 

lista = []
sair = "S"
while sair == "S":
    num = input("Digite um numero: ")
    sair = input("Deseja inserir mais um numero? (S/N): ")
    if sair not in ("N", "S"):
        print("Por favor escolha S ou N")
        sair = "S"
    else:
        lista.append(num)

lista.sort()        
print(lista)


numeros = "4,3,5,7,2,1,0,8"
print(numeros)
lista = numeros.split(",")
lista.sort()
print(lista)