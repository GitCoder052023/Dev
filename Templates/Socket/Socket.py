def setup_socket_files():
    # Create server.py file
    with open("server.py", "w") as server_file:
        server_code = """
# Inside server.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data from client: {data}")

        # Send a response back to the client
        response = "Hello from the server!"
        client_socket.send(response.encode('utf-8'))

        # Close the connection with the client
        client_socket.close()

if __name__ == "__main__":
    start_server()

"""
        server_file.write(server_code)

    # Create client.py file
    with open("client.py", "w") as client_file:
        client_code = """
# Inside client.py
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Send a message to the server
    message = "Hello from the client!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent message to server: {message}")

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response from server: {response}")

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    start_client()

"""
        client_file.write(client_code)

    print("Socket files created: server.py and client.py")