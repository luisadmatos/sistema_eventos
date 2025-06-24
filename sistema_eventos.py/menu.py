import events, participants, reports
from util import limpar_tela

def main_menu():
    limpar_tela()
    options = {
        '1': events.submenu_events,
        '2': participants.submenu_participants,
        '3': reports,
        '4': exit_program

    }

    #fazer o menu mais bonito
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
            input("Pressione Enter para continuar...")#para a mensagem nao sumir

def exit_program():
    print('Saindo...')

main_menu()

