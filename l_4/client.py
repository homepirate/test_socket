import socket
import pickle

HOST = ('localhost', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)

data = 'Hello World'*1024*1024*10
client.send(data.encode('UTF-8'))