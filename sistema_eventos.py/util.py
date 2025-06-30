import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print(f'Campos atualizados: {", ".join(updated)}')
    else:
        print('Nenhuma mudança foi feita')

def list_events(events):
    clear_screen()
    print('-----EVENTOS-----')

    if not events:
        print("Nenhum evento cadastrado.")
        return
    else:
        # Função auxiliar para ordenação que trata datas string e datetime
        def get_date_for_sorting(event):
            date_obj = event['date']
            if hasattr(date_obj, 'strftime'):  # É datetime
                return date_obj
            else:  # É string, tentar converter
                try:
                    from datetime import datetime
                    return datetime.strptime(str(date_obj), '%d/%m/%Y')
                except:
                    from datetime import datetime
                    return datetime.min  # Data mínima se não conseguir converter
        
        ordered_events = sorted(events, key=get_date_for_sorting)

        for i, e in enumerate(ordered_events, 1):
            # Tratar caso onde a data pode ser string ou datetime
            if hasattr(e['date'], 'strftime'):
                date_str = e['date'].strftime('%d/%m/%Y')
            else:
                date_str = str(e['date'])
            print(f"{i}. {e['name']} - {date_str} - {e['location']}")
    print()
    pause()
