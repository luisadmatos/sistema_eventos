import events, participants, reports
from util import limpar_tela

events = {}
participants = {}

def submenu_events():
    options = {
        '1': list_events,
        '2': add_event,
        '3': remove_event,
        '4': att_event, 
        '5': lambda: None
    }

    while True:
        limpar_tela()
        print(
        ''' 
        ----EVENTOS----
        1- Listar Eventos
        2- Adicionar Eventos
        3- Remover Eventos
        4- Atualizar Evento
        5- Voltar
       ----------------
       '''
        )

        choice = input('Escolha uma opção: ').strip()
        action = options.get(choice)

        if action:
            if choice == '5':
                break
            action()
        else:
            print('Opção inválida!')


def submenu_participants():
    options = {
        '1': list_partic,
        '2': add_partic,
        '3': remove_partic,
        '4': att_info,
        '5': verify_duplicate, 
        '6': lambda: None #voltar
    }

    while True:
        limpar_tela()
        print(
        ''' 
        ----PARTICIPANTES----
        1- Listar Participantes
        2- Adicionar Participantes
        3- Remover Participantes
        4- Atualizar Cadastro
        5- Verificar Participantes Duplicados
        6- Voltar
       ----------------
       '''
        )


def main_menu():
    limpar_tela()
    options = {
        '1': events,
        '2': participants,
        '3': reports,
        '4': exit_program

    }

    while True:
        limpar_tela()
        print(
        ''' 
        ----MENU PRINCIPAL----
        1- Gerenciar Eventos
        2- Gerenciar Participantes
        3- Relatórios
        4- Sair
       ------------------------
       '''
       )

        choice = input('Escolha uma opção: ').strip()

        action = options.get(choice)

        if action:
            if choice == "4":
                action()
                break
            else:
                action()
        else:
            print("Opção inválida!") #verificar quando for feita alguma entrada invalida

def exit_program():
    print('Saindo...')

            

