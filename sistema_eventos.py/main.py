# ============================================
# IMPORTS
# ============================================
import events
import participants
import reports
from util import clear_screen

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def exit_program():
    """Exibe mensagem de saída e encerra o programa"""
    print('Saindo...')

# ============================================
# MENU PRINCIPAL
# ============================================

def main_menu():
    """
    Exibe o menu principal do sistema e gerencia a navegação entre os módulos.
    
    O usuário pode escolher entre:
    - Gerenciar Eventos
    - Gerenciar Participantes  
    - Relatórios
    - Sair do programa
    """
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

        if choice == '1':
            events.submenu_events()
        elif choice == '2':
            participants.submenu_participants()
        elif choice == '3':
            reports.submenu_reports()
        elif choice == '4':
            exit_program()
            break
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
*I used 'try' and 'except' instead of 'if/elif' conditionals 
to improve the system's error handling and prevent it from crashing;
*The use of 'action( )' improves the code because it also reduces the use of conditionals
since it takes the dictionary with options.get and executes it;
*The use of functions such as 'clear_screen()', 'split()' and 'strip()' were used to improve 
the readability of the system in the terminal;
*the use of 'key=lambda' in reports.py was to help sort the elements since it receives a 
function to apply to each element and determine its sorting criteria.

'''