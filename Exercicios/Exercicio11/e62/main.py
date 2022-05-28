#main.py

import medicos
import cadastro_plano

usuario = str(input('Digite seu numero de usuario: '))
if usuario in cadastro_plano.usuarios.keys():
    if usuario == '001':
        usuario = 'Victor'
    if usuario == '002':
        usuario = 'Marieli'
    print('Bem vindo(a)', usuario)
else:
    print('Usuário não cadastrado')

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper().strip()

if menu == 'S':
    paciente = input('Por favor digite seu nome: ')
    print(f'{paciente}, escolha qual medico deseja consultar:')
    print('1-Dr. Pimpolho')
    print('2-Dra. Zuleide')
    medico = int(input('Com qual medico deseja agendar uma consulta?'))
    if medico ==1:
        print(f'Sua consulta com o {medicos.medis[0]} sera agendada')
    if medico ==2:
        print(f'Sua consulta com a {medicos.medis[1]} sera agendada')

else:
    print('Agradecemos o seu contato')