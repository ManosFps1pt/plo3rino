import socket

HOST = "192.168.1.78"
PORT = 4070

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(f"hi, what's up?".encode("UTF-8"))
print(client.recv(1024).decode("UTF-8"))
