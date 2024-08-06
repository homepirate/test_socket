import socket
import pickle

HOST = ('localhost', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

resp = client.recv(4096)
print(resp)
print(pickle.loads(resp))
print(type(pickle.loads(resp)))