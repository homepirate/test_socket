import socket


HOST = ('localhost', 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()
print('I`m listening')

while True:
    conn, addr = s.accept()
    print(f'Connecting {addr}')
    print('Waiting for request!!!')

    req = ''
    while True:
        data = conn.recv(4096)
        if not len(data):
            break
        req += data.decode()
    print(req)
    conn.close()
