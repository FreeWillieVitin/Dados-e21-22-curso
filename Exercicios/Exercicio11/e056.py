# 56. Crie uma função com dois paramentros, 
# sendo um deles com um dado valor predeterminado. 

def boas_vindas(nome,nacionalidade='Brasileiro'):
    print(f'Olá: {nome} voce é: {nacionalidade}')

nome = input("Digite seu nome:")
# ex1 = boas_vindas(nome)

nac = input("Digite sua nacionalidade:")
ex2 = boas_vindas(nome,nac)

