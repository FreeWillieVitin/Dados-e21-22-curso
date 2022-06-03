#e_070.py
#Crie uma classe biblioteca que possui uma estrutura molde básica para cadastro de um livro de acordo com seu titulo,
#porem que espera a inclusao de um número não definido de titulos. Em seguida castre ao menos 5 livros nessa biblioteca. (11)
biblioteca = []

class Biblioteca():
    sair = "S" or "s"
    while sair == "S" or "S":
        livro = input("Adicione um livro: ")
        biblioteca.append(livro)
        sair = input("Voce quer adicionar mais um livro ")
        if sair == 'N' or 'n':
            break
        else:
            livro = input("Adicione um livro: ")
            biblioteca.append(livro) 
print(biblioteca)
    
      