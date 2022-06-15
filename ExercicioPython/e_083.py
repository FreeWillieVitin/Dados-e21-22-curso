#e_083.py
from ast import Num


def teste(numero):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while numero:
        div = numero // num[i]
        numero %= num[i]
  
        while div:
            print(rom[i], end = "")
            div -= 1
        i -= 1
  

a = int(input('Digite um numero: '))
b = (teste(a))

