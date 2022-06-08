#Parametros são atributos da classe
class Pessoa:
  def __init__(self,nome,idade,sexo=False,altura=False):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.altura = altura

pessoa1 = Pessoa('Victor', 47, 'M', 1.74)
pessoa2= Pessoa('Marieli', 23)

print(pessoa1.nome,pessoa1.idade,pessoa1.sexo,pessoa1.altura)
print(pessoa2.nome,pessoa2.idade,pessoa2.sexo,pessoa2.altura)
