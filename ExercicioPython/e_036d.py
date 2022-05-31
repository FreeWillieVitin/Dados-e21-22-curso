#e_036d.py

from re import T


frase = str (input('Digite uma palavra ou frase')).strip().upper()
print(frase)
print(type(frase))

palavras = frase.split(sep=';')
print(palavras)
print(type(palavras))