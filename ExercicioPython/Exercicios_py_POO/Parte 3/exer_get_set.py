#exer_get_set.py

from unittest import result


class Calculadora:
    result = 0
    operadores = {'+', '-', '*', '/'}

    def __init__(self, op, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        cal = str(num1) + str(self.op) + str(num2)
        self.result = eval(cal)

    @property
    def aceita(self):
        return self.result

    @aceita.setter
    def aceita(self, valor):
        if isinstance(valor,str):
            valor 

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
op = input('Informe o operador: ')

resultado = Calculadora(op, num1, num2)
print(resultado.result)