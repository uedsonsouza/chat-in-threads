# Chat em Python usando Sockets e Threads

Este projeto implementa um sistema de chat simples usando sockets e threads em Python. O servidor pode aceitar conexões de vários clientes e retransmitir mensagens de um cliente para todos os outros.

## Estrutura do Projeto

- `server.py`: Código do servidor que gerencia as conexões dos clientes e retransmite mensagens.
- `client.py`: Código do cliente que se conecta ao servidor e permite enviar e receber mensagens.

## Requisitos

- Python 3.x

## Como Executar

### Servidor

1. Execute o servidor em uma máquina (VM):

    ```bash
    python server.py
    ```

    O servidor será iniciado e aguardará conexões de clientes na porta `5555`.

### Cliente

1. Nas outras máquinas (VMs), execute os clientes:

    ```bash
    python client.py
    python user.py
    ```

    Certifique-se de substituir `'IP'` pelo endereço IP da máquina onde o servidor está em execução.

## Funcionalidades

- **Servidor**:
    - Aceita múltiplas conexões de clientes.
    - Retransmite mensagens de um cliente para todos os outros.

- **Cliente**:
    - Conecta-se ao servidor.
    - Envia mensagens ao servidor.
    - Recebe mensagens do servidor e as exibe.

## Exemplo de Uso

1. Inicie o servidor:

    ```bash
    python server.py
    ```

2. Inicie os clientes:

    ```bash
    python client.py
    python user.py
    ```
