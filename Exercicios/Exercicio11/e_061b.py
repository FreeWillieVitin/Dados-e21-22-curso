#e_061b.py

def fibo(n):
    print(':', n, end=' ')
    if n <= 1:
        return n
    else:
        ret = fibo(n-1) + fibo(n-2)
        return ret

num = int(input('Digite um numero: '))
x = fibo(num-1)
print("fim:", x)