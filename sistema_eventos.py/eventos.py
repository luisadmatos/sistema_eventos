
from util import limpar_tela

def cadastro_eventos(eventos):
    limpar_tela()
    print('-----CADASTRO DE EVENTOS-----')
    nome = input('Digite o nome do evento: ').strip() 
    tipo = input('Digite o tipo do evento: ').strip() #workshop, palestra, minicurso, etc
    data = input('Digite a data que o evento ocorrerá: ').strip() #melhorar
    tema = input('Digite o tema central do evento: ').strip()

    #continuar

    eventos.append({
        'nome': nome,
        'tipo': tipo,
        'data': data,
        'tema': tema
    })
'''
ideias

- importar algum tipo de verificação para que apenas os usuarios responsaveis pelo cadastro de eventos possa realizar isso
- colocar algum tipo de calendario para não ser preciso digitar manualmente a data desejada
- estipular uma data para o evento ex: 14 a 19 de junho
- ao inves de digitar o tipo de evento, colocar uma maneira melhor (listar os tipos para o user escolher?)
- funcionalidade para voltar ao menu
-

'''