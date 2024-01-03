import socket

def send_command(command):
    host = 'ip_do_servidor'  # Substitua pelo IP do computador que está executando o script
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(command.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    command_to_send = input("Digite um comando para enviar: ")
    send_command(command_to_send)
