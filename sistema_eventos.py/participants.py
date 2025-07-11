# ============================================
# IMPORTS
# ============================================
from util import clear_screen, pause, update_infos
from events import events

# ============================================
# GLOBAL VARIABLES
# ============================================
participants = {}

# ============================================
# AUXILIARY FUNCTIONS
# ============================================

def find_by_cpf(cpf):
    """Search for a participant by CPF"""
    return participants.get(cpf.strip())

def cpf_is_valid(cpf):
    """Validates that the CPF is in the correct format (11 numeric digits)"""
    return cpf.isdigit() and len(cpf) == 11

# ============================================
# PARTICIPANT MANAGEMENT FUNCTIONS
# ============================================

def list_partic_by_event(participants):
    """List of participants registered for a specific event"""
    clear_screen()
    print('''
        =================================  
        LISTA DE PARTICIPANTES POR EVENTO
        ================================= 
        ''')

    event_name = input('Informe o nome do evento: ').strip()

    founded = []

    for cpf, data in participants.items():
        events = [e.lower() for e in data.get('wishlist', ())]

        if event_name.lower() in events:
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


def add_partic(participants):
    """Register a new participant in the system"""
    clear_screen()
    print('''
        =================================  
            CADASTRO DE PARTICIPANTE
        ================================= 
        ''')
    
    cpf = input('Informe o CPF do participante (apenas números): ')

    if not cpf_is_valid(cpf):
        print('CPF inválido. Deve conter 11 números.')
        pause()
        return

    if cpf in participants:
        print('Participante já cadastrado!')
        pause()
        return
    
    name = input('Informe o nome: ')
    email = input('Informe o email: ')

    # Show available events
    print('''
        =================================  
              EVENTOS DISPONÍVEIS
        ================================= 
        ''')
    if not events:
        print("Nenhum evento cadastrado.")
    else:
        from datetime import datetime
        for i, e in enumerate(events, 1):
            if isinstance(e['date'], datetime):
                date_str = e['date'].strftime('%d/%m/%Y')
            else:
                date_str = str(e['date'])
            print(f"{i}. {e['name']} - {date_str} - {e['location']}")
    print('--------------------------------')

    wishlist = input('Qual (is) evento (s) deseja participar? (digite os nomes separados por vírgula): ') 
    chosen_events = [e.strip() for e in wishlist.split(',')]

    participants[cpf] = {
        'name': name.strip(),
        'email': email.strip(),
        'wishlist': chosen_events
    }

    print(f'{name} cadastrado com sucesso!')
    pause()


def update_participant_info(participants):
    """Update the information of an existing participant"""
    clear_screen()
    print('''
        =================================  
              ATUALIZAR CADASTRO
        ================================= 
        ''')

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


def remove_partic(participants):
    """Remove a participant from the system"""
    clear_screen()
    print('''
        =================================  
            REMOVER PARTICIPANTE
        ================================= 
        ''')

    cpf = input('Informe o CPF do participante a ser removido: ')

    if not cpf_is_valid(cpf):
        print('CPF inválido. Deve conter 11 números. ')
        pause()
        return
    
    if cpf in participants:
        confirm = input(f'Tem certeza que deseja remover {participants[cpf]["name"]}? (s/n)').strip()
        if confirm == 's':
            del participants[cpf]
            print('Participante removido com sucesso')
        else:
            print('Remoção cancelada. ')
    else:
        print('CPF não encontrado. Tente novamente')
        return
    
    pause()


def verify_duplicate():
    """Checks and removes duplicate participants in the system"""
    clear_screen()
    print('''
        =================================  
        VERIFICAR E REMOVER DUPLICATAS
        ================================= 
        ''')

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
        print('\nTodos os registros duplicados foram removidos.')

    pause()

# ============================================
# MAIN MENU
# ============================================

def submenu_participants():
    """Main menu for managing participants"""
    options = {
        '1': list_partic_by_event,
        '2': add_partic,
        '3': remove_partic,
        '4': update_participant_info,
        '5': lambda: None  
    }

    while True:
        clear_screen()
        print('''
        ===================================== 
                    PARTICIPANTES
        =====================================  
        1- Listar Participantes
        2- Adicionar Participantes
        3- Remover Participantes
        4- Atualizar Cadastro
        5- Voltar  
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
