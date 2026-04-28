import socket

# Create UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
serverSocket.bind(("192.168.179.128", 9090))

print("UDP server is running...")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Received from client:", message.decode())

    response = "Hello back from Allen"
    serverSocket.sendto(response.encode(), clientAddress)
