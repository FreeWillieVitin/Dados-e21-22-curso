# mULTIPLOS METODOS DE CLASSE

class Pessoa:
  ano_atual=2022

  def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
  
  def ano_nascimento(self):
      ano_nasc = self.ano_atual - self.idade
      print(f'{self.nome}Seu ano de nascimento é {ano_nasc}')

p1 = Pessoa('Victor', 24)

print(p1.ano_nascimento())
