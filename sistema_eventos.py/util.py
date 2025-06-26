import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else clear)


def update_infos(subject: dict, fields: dict):
    for key_field, identifier in fields.items():
        current_value = subject.get(key_field, " ")
        new_value = input(f'{identifier} [{current_value}]: ').strip()
        if new_value:
            subject[key_field] = new_value

