def setup_group_connection():
    # Create server.py file
    with open("server.py", "w") as server_file:
        server_code = """
# server.py
import socket
import threading

# Constants
HOST = '127.0.0.1'
PORT = 12345

# List to store connected clients
clients = []


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            # Broadcast the message to all other clients
            for c in clients:
                if c != client_socket:
                    c.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    # Remove the client from the list
    clients.remove(client_socket)
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")
        clients.append(client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
            """
        server_file.write(server_code)

    with open("client.py", "w") as client_file:
        client_code = """
# client.py
import socket
import threading

# Constants
HOST = '127.0.0.1'  # Change this to the server's IP address
PORT = 12345        # Change this to the server's port number

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Message from {HOST}: {message}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter your message>> ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
        
        """

        client_file.write(client_code)

    print("Socket files created: server.py and client.py")