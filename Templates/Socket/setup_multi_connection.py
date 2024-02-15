

import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client, address = server_socket.accept()
        print(f"Connected to: {address[0]}:{address[1]}")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == '__main__':
    main()
"""

    server_file.write(server_code)

    # Create client.py file
    with open("client.py", "w") as client_file:
        client_code = """
import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, Server!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

    client_socket.close()

if __name__ == '__main__':
    main()
  
        """
    client_file.write(client_code)

    print("Multi connection Socket files created: server.py and client.py")