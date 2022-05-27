#efor_loops_c.py

alunos = {
    'Victor': 'reprovado',
    'Luiz': 'Aprovado',
    'Marieli': 'Aprovado'
    }

for nome, status in alunos.items():
    print(nome, status)

    if status == 'Aprovado':
        print('Parabens:', nome)