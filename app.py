# File: app.py
from flask import Flask, render_template, request
import socket
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-request', methods=['POST'])
def send_request():
    use_nagle = request.form.get('nagle') == 'on'
    num_packets = 50
    packet_size = 100
    message = 'X' * packet_size

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if not use_nagle:
        # Disable Nagle's algorithm using TCP_NODELAY
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    try:
        client_socket.connect(('localhost', 9000))
        
        start_time = time.time()
        
        for i in range(num_packets):
            client_socket.sendall(message.encode())
            time.sleep(0.05)  # Simulate small delay between sends
        
        response = client_socket.recv(1024)
        end_time = time.time()
        
        rtt = end_time - start_time
        nagle_status = "enabled" if use_nagle else "disabled"
        
        return f"Server Response: {response.decode()} | RTT: {rtt:.5f} seconds | Nagle: {nagle_status}"
    except ConnectionRefusedError:
        return "Error: Could not connect to the server. Make sure the server is running."
    finally:
        client_socket.close()

if __name__ == "__main__":
    app.run(port=5001, debug=True)

# File: server.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9000))
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