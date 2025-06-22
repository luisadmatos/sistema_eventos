
from util import limpar_tela
#cadastro de participante 

def cadastro_participantes(participantes):
    limpar_tela()
    print('-----CADASTRO DE PARTICIPANTES-----')
    
    cpf = input('Informe o CPF do participante (apenas números): ')

    if cpf in participantes:
        print('Participante já cadastrado!') 
        return
    
    nome = input('Informe o nome: ')
    email = input('Informe o email: ')
    eventos_desejados = input('Qual (is) evento (s) deseja participar?') #listar eventos existentes?

    participantes[cpf] = {
        'nome': nome.strip(),
        'email': email.strip(),
        'eventos_desejados': [e.strip() for e in eventos_desejados.split()]
    }

    print(f'{nome} cadastrado com sucesso!')

'''
-pensar em verificação se evento existe ou listagem de eventos existentes. 
-cadastrar diretamente no evento ou continuar com o cadastro geral e dps escolha de evento?
-colocar a opção de tipo de evento e os nomes deles 
'''