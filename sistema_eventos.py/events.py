
from util import limpar_tela

events = []

def find_event_by_code(code):
    for event in events:
        if event['code'] == code:
            return event
    return None

def list_events():
    limpar_tela()
    print('-----EVENTOS-----')

    print('\n'.join(
        f"{i}. {e['name']} - {e['date']} - {e['location']}"
        for i, e in enumerate(events, 1)
    ))

    print()


def add_event():
    limpar_tela()
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
    date = input('Digite a data que o evento ocorrerá: ').strip() #melhorar
    location = input('Digite o local do evento: ').strip()

    #continuar

    events.append({
        'code': code,
        'name': name,
        'theme': theme,
        'date': date,
        'location': location

    })

    print(f'\nEvento {name} cadastrado com sucesso!')


def remove_event():
    print('-----REMOVER EVENTO-----')

    try:
        code = int(input('Informe o código do evento: ').strip())
    except ValueError:
        print('Código inválido!')
        return
    
    event = find_event_by_code(code)
    if not event:
        print('Evento não encontrado!')
        return
    
    events.remove(event)
    print(f'\nEvento {code} removido com sucesso!')


def att_event():
    print('-----ATUALIZAR EVENTO-----')

    try:
        code = int(input('Informe o código do evento que deseja atualizar: '))
    except ValueError:
        print('Código Inválido!')
        return
    
    event = find_event_by_code(code)
    if not event:
        print('Evento não encontrado')
        return
    
    print(f'Evento encontrado!')
    print('Deixe em branco os campos que não deseja alterar.')

    #continuar
    

def submenu_events():
    options = {
        '1': list_events,
        '2': add_event,
        '3': remove_event,
        '4': att_event, 
        '5': lambda: None
    }

    while True:
        limpar_tela()
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
'''
ideias

- importar algum tipo de verificação para que apenas os usuarios responsaveis pelo cadastro de eventos possa realizar isso
- colocar algum tipo de calendario para não ser preciso digitar manualmente a data desejada
- estipular uma data para o evento ex: 14 a 19 de junho
- ao inves de digitar o tipo de evento, colocar uma maneira melhor (listar os tipos para o user escolher?)
- funcionalidade para voltar ao menu
-

'''