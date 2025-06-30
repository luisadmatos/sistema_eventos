from collections import Counter
from util import clear_screen, pause
from participants import participants
from events import events

def submenu_reports():
    clear_screen()

    options = {
        '1': report_most_actives,
        '2': report_most_frequent,
        '3': report_events_by_theme,
        '4': report_events_by_date,
        '5': report_low_attendance_events,
        '6': report_rate_by_theme,
        '7': lambda: None
    }

    while True:
        clear_screen()
        print('''
            =================================  
                        RELATÓRIOS
            =================================  
            1. Participantes mais ativos
            2. Eventos mais frequentes
            3. Eventos por tema
            4. Eventos por data
            5. Eventos com baixa procura
            6. Taxa de participação por tema
            7. Voltar
        ''')

        choice = input('Escolha uma opção: ').strip()

        action = options.get(choice)

        if action:
            if choice == "7":
                action()
                break
            else:
                action()
        else:
            print("Opção inválida!") 
            pause()


def report_most_actives():
    clear_screen()
    print('====PARTICIPANTES MAIS ATIVOS====')

    ranked = sorted(participants.items(), key=lambda p: len(p[1].get('wishlist',[])), reverse=True)
    if not ranked:
        print('Nenhum participante cadastrado.')
    else:
        for cpf, data in ranked:
            print(f'{data["name"]} (CPF: {cpf})- {len(data.get("wishlist", []))} eventos')
    
    pause()

def report_most_frequent():
    clear_screen()
    print('==== EVENTOS MAIS PROCURADOS ====')

    all_events = []
    for data in participants.values():
        all_events.extend(data.get('wishlist', []))

    count = Counter(all_events)

    if not count: 
        print('Nenhum evento com participação')
    else:
        for event, qty in count.most_common():
            print(f'{event} - {qty} participantes')
    
    pause()


def report_events_by_theme():
    clear_screen()
    print('====EVENTOS POR TEMA===')

    tema_map = {}
    for event in events:
        tema = event['theme']
        tema_map.setdefault(tema, []).append(event)
    
    for theme, group in tema_map.items():
        print(f'{theme}')
        for e in group:
            print(f'- {e["name"]} em {e["date"].strftime("%d/%m/%Y")}')

    pause()

def report_events_by_date():
    clear_screen()
    print('====EVENTOS POR DATA====')

    if not events:
        print('Nenhum evento cadastrado.')
    else:
        ordered = sorted(events, key=lambda e: e['date'])
        for e in ordered:
            print(f'{e["date"].strftime("%d/%m/%Y")} - {e["name"]} ({e["theme"]})')
    
    pause()

def report_low_attendance_events():
    clear_screen()
    print('====EVENTOS COM BAIXA PROCURA====')

    participation_count = {event['name']: 0 for event in events}

    for data in participants.values():
        for wishlist_event in data.get('wishlist', []):
            if wishlist_event in participation_count:
                participation_count[wishlist_event] += 1
    
    low_interest = [(name, count) for name, count in participation_count.items() if count <= 2]

    if not low_interest:
        print('Nenhum evento com baixa procura foi encontrado.')
    else:
        for name, count in low_interest:
            print(f'- {name}: {count} participante(s) interessado(s)')

        print(f'\nTotal de eventos com baixa procura: {len(low_interest)}')
        print(f'ATENÇÃO! Necessário avaliar a possibilidade de cancelamento do evento devido a baixa adesão!')
    pause()

def report_rate_by_theme():
    clear_screen()
    print('====TAXA DE PARTICIPAÇÃO POR TEMA====')

    theme_totals = {}
    theme_with_participation = {}

    for event in events:
        theme = event['theme']
        theme_totals[theme] = theme_totals.get(theme, 0) + 1

    for data in participants.values():
        for event_name in data.get('wishlist', []):
            matched = next((e for e in events if e['name'].lower() == event_name.lower()), None)
            if matched:
                theme = matched['theme']
                theme_with_participation[theme] = theme_with_participation.get(theme, 0) + 1

    for theme in theme_totals:
        total = theme_totals[theme]
        with_partic = theme_with_participation.get(theme, 0)
        rate = (with_partic / total) * 100 if total else 0
        print(f'{theme}: {rate:.1f}% de participação')
    
    pause()