#e_036e.py

frase = str (input('Digite uma palavra ou frase')).strip().upper()
print(frase)
print(type(frase))

palavras = frase.split()
print(palavras)
print(type(palavras))

caracteres = ''.join(palavras)#join juntar as palavras ignorandso os espaços
print(caracteres)
print(type(caracteres))