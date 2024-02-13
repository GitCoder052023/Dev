def setup_socket_files():
    # Create server.py file
    with open("server.py", "w") as server_file:
        server_code = """
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
        # Add your server logic here

if __name__ == "__main__":
    start_server()
"""
        server_file.write(server_code)

    # Create client.py file
    with open("client.py", "w") as client_file:
        client_code = """
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")
    # Add your client logic here

if __name__ == "__main__":
    start_client()
"""
        client_file.write(client_code)

    print("Socket files created: server.py and client.py")