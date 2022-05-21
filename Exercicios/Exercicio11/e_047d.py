#e_047d.py

aluno = [{
    'Nome': 'Victor', 
    'Notas': [4.7,37.9,79.2]    
    }]

for i in aluno:
    print(f"aluno --> {i['Nome']}")
    print(f"Notas --> {i['Notas']}")
    soma = sum(i["Notas"])
    print(f"Soma ---> {soma}")
    qtditens = len(i['Notas'])
    print(f"")
#notas = []
#notas.append({'Media das notas': 40}) 
#print(notas)