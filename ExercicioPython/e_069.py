#e_069.py
#Crie uma classe Inventario com os atributos de classe pré definidos item1 e item2,
#a serem cadastrados manualmente pelo usuario, simulando um simples carrinho de compras.

class Inventario:
  def __init__(self,item1,item2):
    self.item1 = item1
    self.item2 = item2

item1 = input('Digite um item: ')
item2 = input('Digite um item: ')

print(f'Produto {item1} e produto {item2} foram cadastrados')

