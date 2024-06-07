import socket
import threading

clients = []  # Lista para armazenar os sockets dos clientes conectados

def broadcast(message, client_socket):
    # Enviar a mensagem para todos os clientes, exceto o remetente
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break

def main():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Servidor iniciado e aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexão estabelecida com {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()
