#e_078.py
#Escreva um programa que recebe um texto do usuário e o converte para código morse, 
#exibindo em tela o texto em formato Morse, segundo a padronização '.-' (Ponto, traço)

morse = ' '

Cod_morse = { 'A':'.-', 'B':'-...',
			'C':'-.-.', 'D':'-..', 'E':'.',
			'F':'..-.', 'G':'--.', 'H':'....',
			'I':'..', 'J':'.---', 'K':'-.-',
			'L':'.-..', 'M':'--', 'N':'-.',
			'O':'---', 'P':'.--.', 'Q':'--.-',
			'R':'.-.', 'S':'...', 'T':'-',
			'U':'..-', 'V':'...-', 'W':'.--',
			'X':'-..-', 'Y':'-.--', 'Z':'--..',
			'1':'.----', '2':'..---', '3':'...--',
			'4':'....-', '5':'.....', '6':'-....',
			'7':'--...', '8':'---..', '9':'----.',
			'0':'-----', ', ':'--..--', '.':'.-.-.-',
			'?':'..--..', '/':'-..-.', '-':'-....-',
			'(':'-.--.', ')':'-.--.-'}
texto1 = input('Digite aqui o texto: ').upper()

for i in texto1:    
    morse = Cod_morse[i]
    if i != " ":
        print("{} = {}".format(i, morse))
    else:
        print(morse)
