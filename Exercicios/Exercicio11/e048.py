# e048.py
'''
48. Crie um sistema de perguntas e respostas que interage com o usuário,
pedindo que o mesmo insira uma resposta. Caso a primeira questão esteja
correta, exiba em tela uma mensagem de acerto e vá para  a proxima pergunta,
caso incorreta, exiba uma mensagem de erro e pule para a proxima pergunta.
'''

base = {
    'Pergunta 01':  # A2
    {
        'pergunta': 'Quanto é 4 x 4?',
        'alternativas': {
            'a': '12',
            'b': '24',
            'c': '16',
            'd': '20'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 02': {
        'pergunta': 'Quanto é 6/3',
        'alternativas': {
            'a': '2',
            'b': '1',
            'c': '3',
            'd': '4'
        },
        'resposta_certa': 'a'
    },
}


respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')

    for rkeys, rvalues in pvalues['alternativas'].items():
        # print(f'[{rkeys}]:{rvalues}')

    resposta = input('Escolha uma alternativa: [a],[b],[c], ou [d]')
        print('')
    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!!!')
            respostas_certas += 1  # Corrigido em 23.05.2022
    else:
        print('Resposta ERRADA')

    if respostas_certas == 0:
        print('Voce não acertou nenhuma questão!')
    elif respostas_certas == 1:
        print('Você acertou apenas uma questão')
    else:
        print(f'Você acertou {respostas_certas}. Parabens!!!!')
    

