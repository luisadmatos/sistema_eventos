
from datetime import datetime
from util import clear_screen, pause, update_infos

# ============================================
# GLOBAL VARIABLES
# ============================================
events = []

# ============================================
# AUXILIARY FUNCTIONS
# ============================================

def find_by_name(name):
    """Searches for an event by name (case insensitive)"""
    name = name.strip().lower()
    matches = [event for event in events if event['name'].strip().lower() == name]
    return matches[0] if matches else None
    
def select_or_create_theme():
    """Select an existing theme or create a new one"""
    themes = ['Inteligência Artificial', 'Web', 'Segurança', 'Banco de Dados', 'Mobile']
    print('''
        =================================  
             TEMAS DISPONÍVEIS
        ================================= 
        ''')

    options = {i+1: theme for i, theme in enumerate(themes)}
    create_option = len(themes) + 1
    options[create_option] = 'Cadastrar novo tema'

    for key, value in options.items():
        print(f'{key}. {value}')

    while True:
        try:
            choice = int(input('Escolha um tema ou cadastre um tema novo: '))
        except ValueError:
            print('Entrada inválida. Digite um número: ')
            continue

        if choice in options and choice != create_option:
            return options[choice]
        
        if choice == create_option:
            new_theme = input('Digite o tema que deseja cadastrar: ').strip()
            if new_theme:
                # Check if the theme already exists (case insensitive)
                tema_existe = False
                for theme in themes:
                    if theme.lower() == new_theme.lower():
                        tema_existe = True
                        break
                
                if tema_existe:
                    print(f'Tema "{new_theme}" já existe!')
                    continue
                themes.append(new_theme)
                print(f'Tema "{new_theme}" cadastrado com sucesso')
                return new_theme
            else:
                print('Tema inválido. Digite novamente.')
            continue

        print('Opção inválida. Tente novamente.')

# ============================================
# EVENT MANAGEMENT FUNCTIONS
# ============================================

def list_events():
    clear_screen()
    print('''
        =================================  
                    EVENTOS
        ================================= 
        ''')

    if not events:
        print("Nenhum evento cadastrado.")
        return
    else:
        # Convert dates to datetime before sorting
        def get_date_for_sorting(event):
            date_obj = event['date']
            if isinstance(date_obj, str):
                try:
                    return datetime.strptime(date_obj, '%d/%m/%Y')
                except ValueError:
                    return datetime.min  # Minimum date for events with an invalid date
            return date_obj

        # Exibir eventos na ordem em que foram cadastrados (sem ordenação complexa)  
        for i, e in enumerate(events, 1):
            date_obj = e['date']
            if isinstance(date_obj, str):
                try:
                    date_obj = datetime.strptime(date_obj, '%d/%m/%Y')
                except ValueError:
                    print(f"{i}. {e['name']} - Data inválida - {e['location']} - Tema: {e.get('theme', 'N/A')}")
                    continue

            print(f"{i}. {e['name']} - {date_obj.strftime('%d/%m/%Y')} - {e['location']} - Tema: {e.get('theme', 'N/A')}")

    print()
    pause()


def add_event():
    """Register a new event"""
    clear_screen()
    print('''
        =================================  
                CADASTRO DE EVENTO
        ================================= 
        ''')

    name = input('Digite o nome do evento: ').strip()
    
    if not name:
        print('Nome do evento não pode estar vazio!')
        pause()
        return
    
    if find_by_name(name):
        print('Evento já cadastrado!')
        pause()
        return
    
    theme = select_or_create_theme()
    
    while True:
        date_str = input('Digite a data que o evento ocorrerá (formato: DD/MM/AAAA): ')
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            now = datetime.now()

            # Check that the date is not too old (more than 100 years in the past)
            if date_obj.year < now.year - 100:
                print('Data muito antiga! Digite uma data válida.')
                continue

            if date_obj < now:
                confirm = input('Esta data já passou. Deseja continuar mesmo assim? (s/n): ').strip().lower()
                if confirm != 's':
                    continue
            
            print('Data válida!')
            break

        except ValueError:
            print('Formato de data incorreto! Tente novamente no formato DD/MM/AAAA. ')

    location = input('Digite o local do evento: ').strip()
    
    if not location:
        print('Local do evento não pode estar vazio!')
        pause()
        return

    events.append({
        'name': name,
        'theme': theme,
        'date': date_obj,
        'location': location

    })

    print(f'\nEvento {name} cadastrado com sucesso!')
    pause()


def update_event():
    """Updates the information of an existing event"""
    clear_screen()
    print('''
        =================================  
                ATUALIZAR EVENTO
        ================================= 
        ''')

    name = input('Informe o nome do evento que deseja atualizar: ').strip()
    
    if not name:
        print('Nome Inválido!')
        pause()
        return
    
    event = find_by_name(name)
    if not event:
        print('Evento não encontrado')
        pause()
        return
    
    print(f'Evento encontrado!')
    print('Deixe em branco os campos que não deseja alterar.')

    # Update name
    new_name = input(f'Nome [{event["name"]}]: ').strip()
    if new_name:
        event['name'] = new_name

    # Update theme
    print('Deseja alterar o tema? (s/n)')
    change_theme = input().strip().lower()
    if change_theme == 's':
        event['theme'] = select_or_create_theme()

    # update theme
    current_date = event['date']
    if isinstance(current_date, datetime):
        date_str = current_date.strftime('%d/%m/%Y')
    else:
        date_str = str(current_date)
    
    new_date = input(f'Data (DD/MM/AAAA) [{date_str}]: ').strip()
    if new_date:
        try:
            date_obj = datetime.strptime(new_date, '%d/%m/%Y')
            now = datetime.now()
            if date_obj < now:
                print('Data inválida, deve ser uma data futura.')
            else:
                event['date'] = date_obj
        except ValueError:
            print('Formato de data incorreto! Data não foi alterada.')

    # Update location
    new_location = input(f'Local [{event["location"]}]: ').strip()
    if new_location:
        event['location'] = new_location
    elif not event.get('location'):  # If the current location is empty
        print('Local não pode estar vazio!')
        new_location = input('Digite um local para o evento: ').strip()
        if new_location:
            event['location'] = new_location

    print('Evento atualizado!')
    pause()


def remove_event():
    """Remove an event from the system"""
    clear_screen()
    print('''
        =================================  
                REMOVER EVENTO
        ================================= 
        ''')

    name = input('Informe o nome do evento: ').strip()
    
    if not name:
        print('Nome do evento não pode estar vazio!')
        pause()
        return
    
    event = find_by_name(name)
    if not event:
        print('Evento não encontrado!')
        pause()
        return
    
    # Show event information
    date_str = event['date'].strftime('%d/%m/%Y') if isinstance(event['date'], datetime) else str(event['date'])
    print(f'\nEvento encontrado:')
    print(f'Nome: {event["name"]}')
    print(f'Tema: {event["theme"]}')
    print(f'Data: {date_str}')
    print(f'Local: {event["location"]}')
    
    confirm = input('\nTem certeza que deseja remover este evento? (s/n): ').strip().lower()
    if confirm != 's':
        print('Remoção cancelada.')
        pause()
        return
    
    events.remove(event)
    print(f'\nEvento {name} removido com sucesso!')
    pause()

# ============================================
# MAIN MENU
# ============================================

def submenu_events():
    """Main menu for event management"""
    options = {
        '1': list_events,
        '2': add_event,
        '3': remove_event,
        '4': update_event,
        '5': lambda: None
    }

    while True:
        clear_screen()
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
                print('Saindo...')
                break
            action()
        else:
            print('Opção inválida!')
            pause()

