#e_066.py

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

person = Pessoa(nome='Victor', idade=24, altura=1.74)
print(person.nome)
print(person.idade)
print(person.altura)