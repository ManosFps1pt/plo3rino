import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 4070
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)

communication_socket, address = server.accept()
print(f"connected to {address}")

while True:
    message = communication_socket.recv(1024).decode("UTF-8")
    if message == DISCONNECT_MESSAGE:
        communication_socket.close()
        print(f"connection with {address} closed")
        break
    else:
        print(f"{address}:\t{message}")
