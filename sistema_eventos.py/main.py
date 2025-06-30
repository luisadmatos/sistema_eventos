import events
import participants
import reports
from util import clear_screen

def main_menu():
    """
    Exibe o menu principal do sistema e gerencia a navegação entre os módulos.
    
    O usuário pode escolher entre:
    - Gerenciar Eventos
    - Gerenciar Participantes  
    - Relatórios
    - Sair do programa
    """
    clear_screen()
    options = {
        '1': events.submenu_events,
        '2': participants.submenu_participants,
        '3': reports.submenu_reports,
        '4': exit_program

    }

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
    """
    Exibe mensagem de saída e encerra o programa.
    """
    print('Saindo...')

if __name__ == '__main__':
    main_menu()

