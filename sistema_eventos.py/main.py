# ============================================
# IMPORTS
# ============================================
import events
import participants
import reports
from util import clear_screen

# ============================================
# AUXILIARY FUNCTIONS
# ============================================

def exit_program():
    """Displays exit message and closes the program"""
    print('Saindo...')

# ============================================
# MAIN MENU
# ============================================

def main_menu():
    """
    Displays the system's main menu and manages navigation between modules.
    
    The user can choose between
    - Manage Events
    - Manage Participants
    - Reports
    - Exit the program
    """
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
            print("Opção inválida!")  
            input("Pressione Enter para continuar...")  

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == '__main__':
    main_menu()

'''
Important:
I used 'try' and 'except' instead of 'if/elif' conditionals 
to improve the system's error handling and prevent it from crashing
'''