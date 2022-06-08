#pessoa_v8.py
class Pessoa:
    ano_atual=2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    # Aqui declaramos que a classe a seguir é dinamica por meio de:
    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual-ano_nascimento
        cls.aee = ano_nascimento + 7
        return cls(nome, idade)

pessoal = Pessoa.ano_nascimento('Victor', 1998)
print(pessoal.idade)
print(pessoal.aee)