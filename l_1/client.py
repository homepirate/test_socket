import socket

HOST = ('localhost', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print(f'Connected to {HOST}')

while True:
    msg = client.recv(8)
    if not len(msg):
        break
    print(msg.decode('UTF-8'), end='')
