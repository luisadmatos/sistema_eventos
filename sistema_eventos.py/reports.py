from util import clear_screen, pause

def submenu_reports():
    clear_screen()

    options = {
        '1': report_most_actives,
        '2': report_most_frequent,
        '3': report_events_by_theme,
        '4': report_events_by_date,
        '5': report_low_attendance_events,
        '6': report_rate_by_theme,
        '7': lambda: None
    }

    while True:
        clear_screen()
        print('''
            =================================  
                        RELATÓRIOS
            =================================  
            1. Participantes mais ativos
            2. Eventos mais frequentes
            3. Eventos por tema
            4. Eventos por data
            5. Eventos com baixa procura
            6. Taxa de participação por tema
            7. Voltar
        ''')

        choice = input('Escolha uma opção: ').strip()

        action = options.get(choice)

        if action:
            if choice == "7":
                action()
                break
            else:
                action()
        else:
            print("Opção inválida!") 
            pause()


def report_most_actives():
    pass

def report_most_frequent():
    pass

def report_events_by_theme():
    pass

def report_events_by_date():
    pass

def report_low_attendance_events():
    pass

def report_rate_by_theme():
    pass