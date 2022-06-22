#e_088.py
"""
88. Escreva uma função que recebe do usuário um número qualquer e retorna para omesmo tal numero elevado ao quadrado (simples ok!). Crie uma documentação para esta função que possa ser acessada pelo usuário diretamente via IDE: (dica docstrings e PEP8)
    1.  def quadrado(num):
    2.  '''
    3.  sjdlfkjasçldfjalçskdfjlçaksdjfçlkasjdflçkasj
    4.  num: inteiro 
    5.  '''
        1.  return num **2 
    6.  Faça o mesmo com uma Class.

    Plus:
        instanciar uma variavel com as classes: dict() e list() e estudar a funcionalidade de cada metodo visivel das classes. 

        '''
        dd = dict()
        dd.clear
        dd.copy
        dd.fromkeys
        dd.get
        dd.?????

        ll = list()
        ll.append
        ll.clear
        ll.count
        ll.extend
        ll.?????

        '''
"""

def docs(num):
    '''Recebe o valor na variavel num, e retorna ao quadrado o valor de num'''
    return num**2

num=int(input("Digite um numero: "))

print(docs(num))

class AoQuadrado:

    def docs(self, num):
        '''Recebe o valor na variavel num, e retorna ao quadrado o valor de num'''
        return num**2

calc = AoQuadrado()

tes=int(input("Digite um numero: "))
print(calc.docs(tes))

