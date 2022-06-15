#e_082c.py

class Teste:
    jacare = 'Amarela'
    print('Escopo 2: ', jacare)
    def __init__(self, jacare):
        print('Escopo 3: ', jacare)
        self.a = jacare

jacare = 'vermelho'

print('Escopo 1: ', jacare)

Teste('Preto')