#e_047b.py

data = {
    'Notas': [],
    'Faltas': []
}
data['Notas'].append('10')
data['Notas'].append('20')
data['Notas'].append('30')
data['Notas'].append('40')
data['Faltas'].append('12')


print(data)
print(type(data))
print(data['Faltas'])
print(type(data['Faltas']))
print(data['Notas'])
print(type(data['Notas']))

n = data['Notas']

for i in range(0, len(n)-1,-1,-1):
    print(n[i])
