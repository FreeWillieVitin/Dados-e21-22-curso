#e_036.py

from ntpath import join


frase = str(input("Digite uma palavra ")).strip().upper()
print(frase)

palavras = frase.split()
print(palavras)
caracteres = ''.join(palavras)
print(caracteres)
fraseinvertida = ''

for i in range(
    len(caracteres)-1,
    -1,
    -1
    ):
    fraseinvertida += caracteres[i]

print(caracteres,fraseinvertida)

if fraseinvertida == caracteres:
    print('é um palindromo')
else:
    print('não é') 