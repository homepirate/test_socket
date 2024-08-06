import socket
import sys

HOST = ('localhost', 10000)
HEADER_LENGTH = 10

username = input('Enter your username: ').encode('UTF-8')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)
client.setblocking(False)
header = f'{len(username):<{HEADER_LENGTH}}'.encode('UTF-8')

client.send(header+username)


while True:
    msg = input("Write msg: ").encode('UTF-8')
    if msg:
        msg_header = f'{len(msg):<{HEADER_LENGTH}}'.encode('UTF-8')
        client.send(msg_header+msg)
    try:
        while True:
            user_header = client.recv(HEADER_LENGTH)
            if not user_header:
                sys.exit()
            user_length = int(user_header.decode('UTF-8').strip())
            username = client.recv(user_length).decode('UTF-8')
            msg_header = client.recv(HEADER_LENGTH)
            msg_length = int(msg_header.decode('UTF-8').strip())

            data = client.recv(msg_length).decode('UTF-8')
            print(f'New message: {username} - {data}')
    except IOError as e:
        pass
