import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9000))  # Changed port to 9000
    server_socket.listen(5)
    print("Server listening on port 9000...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            client_socket.sendall(b"ACK")
        
        client_socket.close()

if __name__ == "__main__":
    start_server()