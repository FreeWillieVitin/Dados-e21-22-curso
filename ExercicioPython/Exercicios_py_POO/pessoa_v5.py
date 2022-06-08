#pessoa_v5.py
class Pessoa:
    def __init__(self, nome, login=False, logoff=False):
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        print(f'Seja Bem vindo {self.nome}, você está logado no sistema.!')
        self.login = True

    
usuario = Pessoa('Victor')
print(usuario.login)

usuario.logar()
print(usuario.login)