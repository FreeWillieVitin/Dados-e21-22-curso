#pandas001.py
from pandasfiles import importa_planilha

#colunas = list(['id', 'Nome', 'Telefone'])
#dd = importa_planilha(colunas)
#print(dd)

exemplo = 3

if(exemplo == 1):
    colunas = list(['id', 'Nome', 'Telefone'])
    dd = importa_planilha(colunas)
    colunas.remove('id')
    #Imprime todos os items
    for i in dd.items():
        print(f' Items: {i} ')
    #Imprime somente os valores
    for i in dd.values():
        print(f' Items: {i} ')

if(exemplo == 2):
    colunas = list(['id', 'Nome', 'Telefone'])
    dd = importa_planilha(colunas)
    print(colunas)
    colunas.remove('id')
    print(colunas)

    for i in dd.values():

        print(
            i['Nome'],
            i['Telefone']
        )

if(exemplo == 3):
    novo_bol = []

    colunas = list(['id', 'Nome', 'Telefone', 'CEP', 'Idade', 'N1', 'N2', 'N3', 'N4'])

    dd = importa_planilha(colunas)

    colunas_nota = list(['N1', 'N2', 'N3', 'N4'])

    colunas.remove('id')

    print('==========================================================')
    for x in colunas:
        print(' ', x, end=' ')
    print('\n---------------------------------------------------------\n')

    for i in dd.values():
        print(":", end=' ')

    for N in colunas:
        print(i[N], end=' ')

    #print()

    soma = 0
    numero = 0

    for M in colunas_nota:
        soma += float(str(i[M]).replace(',', '.'))
        numero += 1
        media = (soma/numero)
        media_redonda = round(media, 2)

        print(f'Some: {round(soma, 1)}, Média: {media_redonda}')

        status = 'Reprovado'
        if(media_redonda>=7):
            status = 'Aprovado'

        novo_bol.append(
            {
                'Nome': i['Nome'],
                'Media': media_redonda,
                'Status': status
            }
        )
        # Ao final do imprime o boletim
    colunas_nota=list(['Nome','Media','Status'])
    print("Boletim:")
    print("======================================")
    for a in colunas_nota:
        print(a,end=' ')    
    
    print("\n--------------------------------------")

    # Aqui percorre o novo dict_boletim:
    # {'Nome': 'Adriano', 'Media': 5.5, 'Status': 'Reprovado'}
    # {'Nome': 'Karina', 'Media': 6.0, 'Status': 'Reprovado'}
    # {'Nome': 'Mario', 'Media': 6.0, 'Status': 'Reprovado'}


    for b in novo_bol:
        for c in colunas_nota:
            print(b[c],end=' ')
        print('')
    print("======================================")