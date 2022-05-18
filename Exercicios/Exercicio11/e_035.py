numero = int(input("Digite um numero"))
divisoes = 0

for i in range(1, numero + 1):
    if numero %i == 0:
        divisoes += 1
        

if divisoes == 2:
    print(f"{numero} é primo")
    print(f"{numero} é divisivel por um ou por {numero}")
else:
    print(f"{numero}NAO é primo")
    print(f"{numero} é divisivel {divisoes} vezes")