#e_036f.py

#range(start, stop, step)
from sys import call_tracing
frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
caracteres = ''.join(palavras)
tamanho = (len(caracteres))

fraseinvertida = ''
for i in range((tamanho-1),-1,-1):
    fraseinvertida += caracteres[i]

if fraseinvertida == caracteres:
    print('É um palindromo!!!')
else:
    print('Não é')
# for i in range (10,0,-1):
#    print(i, end=" ")

# print('\n')

#for i in range (len(caracteres)-1,-1,-1):
 #  print(caracteres[i], end=' ')
 #  x = x + 1
 #  print(x, sep=' ')