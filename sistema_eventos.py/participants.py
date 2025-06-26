
from util import clear_screen
#cadastro de participante 

participants = {}

def submenu_participants():
    options = {
        '1': list_partic,
        '2': add_partic,
        '3': remove_partic,
        '4': att_info,
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
            action()
        else:
            print('Opção inválida!')
            input("Pressione Enter para continuar...")


def list_partic():
    pass
def remove_partic():
    pass
def att_info():
    pass
def verify_duplicate(): 
    pass



def add_partic():
    clear_screen()
    
    print('-----CADASTRO DE PARTICIPANTES-----')
    
    cpf = input('Informe o CPF do participante (apenas números): ')

    if cpf in participants:
        print('Participante já cadastrado!') 
        return
    
    name = input('Informe o nome: ')
    email = input('Informe o email: ')
    wishlist = input('Qual (is) evento (s) deseja participar?') #listar eventos existentes?

    participants[cpf] = {
        'name': name.strip(),
        'email': email.strip(),
        'wishlist': [e.strip() for e in wishlist.split()]
    }

    participants = {
        'name': name.strip(),
        'email': email.strip(),
        'wishlist': [e.strip() for e in wishlist.split()]
    }

    print(f'{name} cadastrado com sucesso!')
    input("Pressione Enter para continuar...")

'''
-pensar em verificação se evento existe ou listagem de eventos existentes. 
-cadastrar diretamente no evento ou continuar com o cadastro geral e dps escolha de evento?
-colocar a opção de tipo de evento e os nomes deles 
'''