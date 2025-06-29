import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)

def pause():
    input('Pressione Enter para continuar...')

def update_infos(subject: dict, fields: dict):
    updated = []

    for key_field, identifier in fields.items():
        current_value = subject.get(key_field, "-----")
        new_value = input(f'{identifier} [{current_value}]: ').strip()
        if new_value:
            subject[key_field] = new_value
            updated.append(key_field)

    if updated:
        print(f'Campos atualizados: {''.join(updated)}')
    else:
        print('Nenhuma mudança foi feita')

def list_events(events):
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
    pause()
