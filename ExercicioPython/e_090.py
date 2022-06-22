#e_090.py
#  Crie um programa que recebe do usuário uma sequencia de números aleatórios separados por vírgula,
#  armazene os números um a um, em formato de texto, como elementos ordenados de uma lista.
#  Mostre em tela a lista com seus respectivos elementos após serem ordenados. 

lista = []
add = "S"
while add == "S":
    lista.append(str(input('Digite um numero: ')))
    input('Deseja inserir mais um numero? (S/N)')
    if add not in ("N", "S"):
        print("Por favor escolha S ou N")
        add = "N"
    else:
        lista.append(str(input('Digite um numero: ')))
    
print(lista)
