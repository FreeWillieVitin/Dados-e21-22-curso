# e048b.py
base = {
    'Pergunta 01': # A2
    {
        'pergunta': 'Quanto é 4 x 4?',  
        'alternativas': {
            'a': '12',
            'b': '24',
            'c': '16',
            'd': '20',
        },
        'resposta_certa': 'c'
    }
}

print(type(base))
respostas_certas = 0 
for x, y in base.items():
    # print(f'x:{x}:Y:{y["pergunta"]}')
    print("ID_Pergunta (Keys X:",x)
    print("    Pergunta (values) Y:",y['pergunta'])
    print("    Pergunta (values) Y:",y['alternativas'])
    
    for A, B in y['alternativas'].items():
        print(f'[{A}]:{B}', end=' ' )
    

    print("    Pergunta (values) Y:",y['resposta_certa'])

    resposta = input('Escolha uma alternativa: [a],[b],[c], ou [d]')
    print('')

    if resposta == y['resposta_certa']:
        print('Resposta Correta!!!')
        respostas_certas += 1  # Corrigido em 23.05.2022
    else:
        print('Resposta ERRADA')


