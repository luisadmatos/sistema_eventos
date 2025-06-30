
from datetime import datetime
from util import clear_screen, pause, update_infos

events = []
   
def find_by_name(name):
    name = name.strip().lower()
    matches = [event for event in events if event['name'].strip().lower() == name]
    return matches[0] if matches else None
    
def select_or_create_theme():
    themes = ['Inteligência Artificial', 'Web', 'Segurança', 'Banco de Dados', 'Mobile']
    print('----Temas disponíveis----')

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
                themes.append(new_theme)
                print(f'Tema "{new_theme}" cadastrado com sucesso')
                return new_theme
            else:
                print('Tema inválido. Digite novamente.')
            continue

        print('Opção inválida. Tente novamente.')
    

def list_events():
    clear_screen()
    print('-----EVENTOS-----')

    if not events:
        print("Nenhum evento cadastrado.")
        return
    else:
        ordered_events = sorted(events, key=lambda e: e['date'])

        for i, e in enumerate(ordered_events, 1):
            print(f"{i}. {e['name']} - {e['date'].strftime('%d/%m/%Y')} - {e['location']}")

    print()
    print(pause())


def add_event():
    clear_screen()
    print('-----CADASTRO DE EVENTOS-----')

    try:
        name = input('Digite o nome do evento: ').strip() 
    except ValueError:
        print('Evento já cadastrado!')
        return
    
    if find_by_name(name):
        print('Evento já cadastrado!')
        return
    
    theme = select_or_create_theme()
    
    while True:
        date_str = input('Digite a data que o evento ocorrerá (formato: DD/MM/AAAA): ')
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            now = datetime.now()

            if date_obj < now:
                print('Data inválida, Digite uma data futura.')
            else: 
                print('Data válida!')
                break

        except ValueError:
            print('Formato de data incorreto! Tente novamente no formato DD/MM/AAAA. ')

    location = input('Digite o local do evento: ').strip()

    events.append({
        'name': name,
        'theme': theme,
        'date': date_obj,
        'location': location

    })

    print(f'\nEvento {name} cadastrado com sucesso!')
    pause()


def remove_event():
    print('-----REMOVER EVENTO-----')

    try:
        name = input('Informe o nome do evento: ').strip()
    except ValueError:
        print('Nome inválido!')
        input("Pressione Enter para continuar...")
        return
    
    event = find_by_name(name)
    if not event:
        print('Evento não encontrado!')
        pause()
        return
    
    events.remove(event)
    print(f'\nEvento {name} removido com sucesso!')
    pause()

def update_event():
    print('-----ATUALIZAR EVENTO-----')

    name = input('Informe o nome do evento que deseja atualizar: ')
    
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

    fields = {
        'name': 'new name',
        'theme': 'new theme',
        'date': 'new date',
        'location': 'new location'
    }

    update_infos(event, fields)

    print('Evento atualizado!')
    pause()
    

def submenu_events():
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
                break
            action()
        else:
            print('Opção inválida!')
            pause()

