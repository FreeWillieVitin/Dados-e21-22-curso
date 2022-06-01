class Pessoa2:
    administrador = 'Admin'

    def __init__(self,nome,msg):
        self.nome = nome
        self.msg = msg
        print('init', msg)

    def metodo1(self):
        print('met1', self.msg)