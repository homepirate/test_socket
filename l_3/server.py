import socket
import pickle

HOST = ('localhost', 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()
print('I`m listening')

d = {
    'name': 'Evgeniy',
    'age': 24
}

while True:
    conn, addr = s.accept()
    print(f'Connected from {addr}')
    conn.send(pickle.dumps(d))
    conn.close()


