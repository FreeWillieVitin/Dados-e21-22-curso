#  57 Crie uma função com tres parametros, sendo dois
#  deles com dados/valores padrão, alterando o terceiro deles
#  contornando o paradigma da justaposição de argumentos. 

def pessoa1(nome,idade=18, funcao='tecnico'):
    print(f'{nome} tem {idade} anos e sua funcao é {funcao}')


p1 = pessoa1('Victor', funcao='Programador')

