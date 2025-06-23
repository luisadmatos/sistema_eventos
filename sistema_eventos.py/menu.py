import events, participants, reports
from util import limpar_tela

events = {}
participants = {}

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

            

