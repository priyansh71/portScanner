import socket

c = socket.socket()
print("Client socket created.")

c.connect(('192.168.172.208', 1235))
print("Sockets connected.")

name = input("Enter your name")
c.send(bytes(name,'utf-8'))

data = c.recv(1024).decode()
print(data)