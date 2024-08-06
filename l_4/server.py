import socket
import select

HEADER_LENGTH = 10
HOST = ('localhost', 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()

print("I am listening!")

socket_list = [s]
client_list = dict()


def receive_msg(client: socket.socket):
    try:
        msg_header = client.recv(HEADER_LENGTH)
        if not msg_header:
            return False

        msg_length = int(msg_header.decode('UTF-8').strip())
        return {
            'header': msg_header,
            'data': client.recv(msg_length)
        }
    except:
        return False


while True:
    rs, _, es = select.select(socket_list, [], socket_list)

    for sck in rs:
        if sck == s:
            client, addr = s.accept()
            print(addr)
            user = receive_msg(client)
            print(user)
            if not user:
                continue
            socket_list.append(client)
            client_list[client] = user
            data = user['data']
        else:
            msg = receive_msg(sck)
            if not msg:
               print('Connection')
               socket_list.remove(sck)
               del client_list[sck]
               continue
            user = client_list[sck]

            for client in client_list:
                client.send(user['header']+user['data']+msg['header']+msg['data'])
    # for sck in es:
    #     socket_list.remove(sck)
    #     del client_list[sck]


