#e_074.py
#Escreva um programa, (calculadora simples), de 4 operações, onde o usuário escolherá entre uma das 4 operacções (+-*/).
#Lembrnado que o usuário digitará apenas dois valroes, e escolhera uma operação de matematica do menu. (22)
class calculadora:
 def __init__(self, soma, sub, mult, div):
        self.soma = soma
        self.sub = sub
        self.mult = mult
        self.div = div

num1 = float(input('Digite o primeiro valor da operação: '))
num2 = float(input('Digite o segundo valor da operação: '))
calculo = calculadora(num1+num2, num1-num2, num1*num2, num1/num2,)
operacao = int(input(f'Digite: 1=soma - 2=subtração - 3=multiplicação - 4=divisão: '))

if operacao == 1:
    print(calculo.soma)
if operacao == 2:
    print(calculo.sub)
if operacao == 3:
    print(calculo.mult)
if operacao == 4:
    print(calculo.div)
if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
    print('Voce não digitou uma opção válida')