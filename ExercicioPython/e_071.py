#e_071.py
#Crie uma calculadora simples de 4 operações (soma,sub,multi e div) usando apenas de estrutura de código orientada a objetos.
#Ex. calc.soma(3,4); calc.div(9,3) (11)
class Calculadora:

    def soma(self, vlr1, vlr2):
        return (vlr1 + vlr2)

    def sub(self, vlr1, vlr2):
        return (vlr1 - vlr2)

    def multi(self, vlr1, vlr2):
        return (vlr1 * vlr2)

    def div(self, vlr1, vlr2):
        return (vlr1 / vlr2)

calc = Calculadora()
print(calc.soma(8,8))
print(calc.sub(8,8))
print(calc.multi(8,8))
print(calc.div(8,8))