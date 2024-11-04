import socket

HOST = "192.168.1.8"
PORT = 4070
DISCONNECT_MESSAGE = "!DISCONNECT"
send_counter = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


with open("../gcode", "r") as file:
    doc = file.read()


client.send(doc.encode("UTF-8"))

client.send(DISCONNECT_MESSAGE.encode("UTF-8"))
print(send_counter)

