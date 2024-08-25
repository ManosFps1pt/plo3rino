import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 4070

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(1)

communication_socket, address = server.accept()
print(f"connected to {address}")
message = communication_socket.recv(1024).decode("UTF-8")
print(f"message from {address} is {message}")
communication_socket.send(f"thx for sending".encode("UTF-8"))
communication_socket.close()
print(f"connection with {address} closed")
