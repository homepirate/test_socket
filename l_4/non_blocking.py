import socket

HEADER_LENGTH = 10
HOST = ('localhost', 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()

print("I am listening!")

while True:
    client, addr = s.accept()
    print(f'Connection {addr}')

    data = client.recv(512)
    while data:
        print(data.decode('UTF-8'))
        data = client.recv(512)

    client.close()
