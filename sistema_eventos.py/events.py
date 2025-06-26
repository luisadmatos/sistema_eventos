
from util import clear_screen
from util import update_infos

events = []
   
def find_event_by_code(code):
    for event in events:
        if event['code'] == code:
            return event
    return None


def list_events():
    clear_screen()
    print('-----EVENTOS-----')

    if not events:
        print("Nenhum evento cadastrado.")
        input("Pressione Enter para continuar...")
    else:
        for i, e in enumerate(events, 1):
            print(f"{i}. {e['name']} - {e['date']} - {e['location']}")

    print()
    input("Pressione Enter para continuar...")


def add_event():
    clear_screen()
    print('-----CADASTRO DE EVENTOS-----')

    try:
        code = int(input('Informe o código do evento: ').strip())
    except ValueError:
        print('Evento já cadastrado!')
        return
    
    if find_event_by_code(code):
        print('Evento já cadastrado!')
        return
    
    name = input('Digite o nome do evento: ').strip() 
    theme = input('Digite o tema central do evento: ').strip()
    date = input('Digite a data que o evento ocorrerá: ').strip() 
    location = input('Digite o local do evento: ').strip()

    events.append({
        'code': code,
        'name': name,
        'theme': theme,
        'date': date,
        'location': location

    })

    print(f'\nEvento {name} cadastrado com sucesso!')
    input("Pressione Enter para continuar...")


def remove_event():
    print('-----REMOVER EVENTO-----')

    try:
        code = int(input('Informe o código do evento: ').strip())
    except ValueError:
        print('Código inválido!')
        input("Pressione Enter para continuar...")
        return
    
    event = find_event_by_code(code)
    if not event:
        print('Evento não encontrado!')
        input("Pressione Enter para continuar...")
        return
    
    events.remove(event)
    print(f'\nEvento {code} removido com sucesso!')
    input("Pressione Enter para continuar...")

def att_event():
    print('-----ATUALIZAR EVENTO-----')

    try:
        code = int(input('Informe o código do evento que deseja atualizar: '))
    except ValueError:
        print('Código Inválido!')
        input("Pressione Enter para continuar...")
        return
    
    event = find_event_by_code(code)
    if not event:
        print('Evento não encontrado')
        input("Pressione Enter para continuar...")
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
    input('Pressione Enter para voltar...')
    

def submenu_events():
    options = {
        '1': list_events,
        '2': add_event,
        '3': remove_event,
        '4': att_event, 
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
            input("Pressione Enter para continuar...")

