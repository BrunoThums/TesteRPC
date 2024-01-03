import socket
import pyautogui

def start_server():
    host = '192.168.56.1'  # Aceita conexões de qualquer endereço
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor aguardando conexão na porta {port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        # Simula a entrada de teclado com pyautogui
        pyautogui.write(data)

    client_socket.close()

if __name__ == "__main__":
    start_server()
