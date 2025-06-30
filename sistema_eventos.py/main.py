import events
import participants
import reports
from util import clear_screen

def main_menu():
    clear_screen()
    options = {
        '1': events.submenu_events,
        '2': participants.submenu_participants,
        '3': reports.submenu_reports,
        '4': exit_program

    }

    #fazer o menu mais bonito
    while True:
        clear_screen()
        print(
        ''' 
        ╔═══════════════════════════════════════════════════════════╗
        ║                                                           ║
        ║            BEM VINDO AO PROJETO COMUNIDADE TECH!          ║
        ║                                                           ║
        ║            Por favor, selecione a opção que deseja:       ║
        ║                                                           ║
        ╠═══════════════════════════════════════════════════════════╣
        ║                                                           ║
        ║   1. Gerenciar Eventos                                    ║
        ║   2. Gerenciar Participantes                              ║
        ║   3. Relatórios                                           ║
        ║   4. Sair                                                 ║
        ║                                                           ║
        ╠═══════════════════════════════════════════════════════════╣
        ║          Utilize o número ao lado da sua preferência      ║
        ╚═══════════════════════════════════════════════════════════╝
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

if __name__ == '__main__':
    main_menu()

