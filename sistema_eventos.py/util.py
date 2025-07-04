# ============================================
# IMPORTS
# ============================================
import os

# ============================================
# UTILITY FUNCTIONS
# ============================================

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause execution until the user presses enter"""
    input('Pressione Enter para continuar...')

def update_infos(subject: dict, fields: dict):
    """
    Updates information in a dictionary based on user input
    
    Args:
    subject (dict): Dictionary to be updated
    fields (dict): Field mapping {key: description_to_user}
    """
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
    """Simple event list (auxiliary function)"""
    clear_screen()
    print('-----EVENTOS-----')

    if not events:
        print("Nenhum evento cadastrado.")
        return
    
    # Easily sort events by date
    ordered_events = []
    for event in events:
        ordered_events.append(event)
    
    # View events
    for i, e in enumerate(ordered_events, 1):
        # Verify if the date is a datetime object or string
        date_obj = e['date']
        from datetime import datetime
        if isinstance(date_obj, datetime):  # it is a datetime object
            date_str = date_obj.strftime('%d/%m/%Y')
        else:  # It is a string
            date_str = str(date_obj)
        
        print(f"{i}. {e['name']} - {date_str} - {e['location']}")
    
    print()
    pause()
