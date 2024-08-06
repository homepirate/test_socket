import socket

HOST = ('localhost', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

sent = 0
request = b'SOME DATA FOR SEND'
# while sent < len(request):
#     sent += client.send(request[sent:])
# одинаково с sendall
client.sendall(request)

print('Send msg!')