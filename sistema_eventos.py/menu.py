import eventos, participantes, consulta_evento, consulta_partic, relatorios
from util import limpar_tela

def menu_principal():
    limpar_tela()
    opcoes = {
        '1': eventos,
        '2': participantes,
        '3': consulta_evento,
        '4': consulta_partic,
        '5': relatorios
    }

    while True:
        limpar_tela()
        print('----MENU PRINCIPAL----')
        print('1- Cadastrar evento')
        print('2- Cadastrar participante')
        print('3- Consulta de eventos')
        print('4- Consulta de participantes')
        print('5- Relatórios')
        print('0- Sair')
        print('----------------------')

        escolha = input('Escolha uma opção: ').strip()

        if escolha == '0':
            print('\nSaindo do sistema... ')
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else: 
            print('\nOpção inválida. Por favor, digite um número de 0 a 5')

            

