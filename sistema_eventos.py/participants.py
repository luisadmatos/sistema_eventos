
from util import clear_screen, list_events, pause, update_infos
from events import events

#cadastro de participante 

participants = {}

def find_by_cpf(cpf):
    return participants.get(cpf.strip())

def cpf_is_valid(cpf):
    if cpf.isdigit() and len(cpf) == 11:
        return True
    print('CPF inválido. Deve conter 11 números. ')
    pause()
    return False

def submenu_participants():
    options = {
        '1': list_partic_by_event,
        '2': add_partic,
        '3': remove_partic,
        '4': update_participant_info,
        '5': verify_duplicate, 
        '6': lambda: None #voltar
    }

    while True:
        clear_screen()
        print(
        ''' 
        ----PARTICIPANTES----
        1- Listar Participantes
        2- Adicionar Participantes
        3- Remover Participantes
        4- Atualizar Cadastro
        5- Verificar Participantes Duplicados
        6- Voltar
       ----------------
       '''
        )

        choice = input('Escolha uma opção: ').strip()
        action = options.get(choice)

        if action:
            if choice == '6':
                break
            action(participants)
        else:
            print('Opção inválida!')
            input("Pressione Enter para continuar...")


def list_partic_by_event(participants):
    clear_screen()
    print('-----PARTICIPANTES POR EVENTO-----')

    event_name = input('Informe o nome do evento: ').strip()

    founded = []

    for cpf, data in participants.items():
        events = [e.lower() for e in data.get('wishlist', ())]

        if event_name in events:
            founded.append((cpf, data['name'], data['email']))

    if founded:
        print(f'Participantes inscritos no evento "{event_name}": ')
        for cpf, name, email in founded:
            print(f'Nome:{name}')
            print(f'CPF:{cpf}')
            print(f'Email:{email}')

    else:
        print(f'Nenhum participante inscrito no evento "{event_name}"') 
    pause()


def remove_partic(participants):
    clear_screen()
    print('-----REMOVER PARTICIPANTE-----')

    cpf = input('Informe o CPF do participante a ser removido: ')

    if not cpf_is_valid(cpf):
        print('CPF inválido. Deve conter 11 números. ')
        pause()
        return
    
    if cpf in participants:
        confirm = input(f'Tem certeza que deseja remover {participants[cpf]['name']}? (s/n)').strip()
        if confirm == 's':
            del participants[cpf]
            print('Participante removido com sucesso')
        else:
            print('Remoção cancelada. ')
    else:
        print('CPF não encontrado. Tente novamente')
        return
    
    pause()

def update_participant_info(participants):
    print('-----ATUALIZAR CADASTRO-----')

    cpf = input('Informe o cpf do participante que deseja atualizar: ')
    
    if not cpf_is_valid(cpf):
        print('CPF Inválido!')
        pause()
        return
    
    participant = find_by_cpf(cpf)
    if not participant:
        print('Participante não encontrado')
        pause()
        return
    
    print(f'Participante encontrado!')
    print('Deixe em branco os campos que não deseja alterar.')

    fields = {
        'email': 'new email',
        'wishlist': 'new wishlist'
    }

    update_infos(participant, fields)

    print('Cadastro atualizado!')
    pause()


def verify_duplicate(): 
    clear_screen()
    print('====VERIFICAR E REMOVER DUPLICATAS====')

    seen = {}
    duplicates = []

    for cpf, data in participants.items():
        key = (data['name'].strip().lower(), data['email'].strip().lower())
        if key in seen:
            duplicates.append(cpf)
        else:
            seen[key] = cpf
    
    if not duplicates:
        print('Nenhum participante duplicado encontrado.')
    else:
        print(f'Foram encontrados {len(duplicates)} participante(s) duplicado(s)\n')
        for cpf in duplicates:
            name = participants[cpf]['name']
            print(f'Removendo duplicata: {name} (CPF: {cpf})')
            del participants[cpf]
        print('\nTodos os registros duplicados foram duplicados foram removidos.')

    pause()

def add_partic(participants):
    clear_screen()
    print('-----CADASTRO DE PARTICIPANTES-----')
    
    cpf = input('Informe o CPF do participante (apenas números): ')

    if cpf in participants:
        print('Participante já cadastrado!')
        pause()
        return
    
    name = input('Informe o nome: ')
    email = input('Informe o email: ')

    list_events(events)

    wishlist = input('Qual (is) evento (s) deseja participar?') 
    chosen_events = [e.strip() for e in wishlist.split(',')]


    participants[cpf] = {
        'name': name.strip(),
        'email': email.strip(),
        'wishlist': chosen_events
    }

    print(f'{name} cadastrado com sucesso!')
    pause()
