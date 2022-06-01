#Ver 1 Classe vazia
#class Pessoa:
#    pass

#Ver 2 Classe com atributo
#class Pessoa:
#    nome = 'Victor'

#Ver 3 Atribuição de metodos(atribuitos de inicializaçao a uma classe)
class Pessoa:
    def __init__(self, nome, idade, altura, cidade):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cidade = cidade