# Sistema de Gerenciamento de Eventos

## Descrição

Sistema simples em Python para gerenciar eventos e participantes de uma comunidade tecnológica.

## Funcionalidades

### Eventos
- Cadastrar novos eventos
- Listar eventos
- Atualizar eventos
- Remover eventos
- Ver detalhes de eventos

### Participantes
- Cadastrar participantes
- Listar participantes por evento
- Atualizar dados de participantes
- Remover participantes
- Verificar duplicatas

### Relatórios
- Participantes mais ativos
- Eventos mais procurados
- Eventos por tema
- Eventos por data
- Eventos com baixa procura
- Taxa de participação por tema

## Como usar

1. Execute o arquivo `main.py`
2. Escolha uma opção do menu principal
3. Siga as instruções na tela

## Estrutura dos arquivos

- `main.py` - Menu principal
- `events.py` - Gerenciamento de eventos
- `participants.py` - Gerenciamento de participantes
- `reports.py` - Relatórios
- `util.py` - Funções auxiliares

## Requisitos

- Python 3.6 ou superior

## Como executar

```bash
cd sistema_eventos.py
python main.py
```

## Validações

- CPF deve ter 11 dígitos
- Datas no formato DD/MM/AAAA
- Campos obrigatórios não podem estar vazios
- Confirmação antes de remover dados