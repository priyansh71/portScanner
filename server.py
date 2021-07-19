import socket

s = socket.socket()
print("Server socket created.")

port = 1235
s.bind(('', port))
print("Server socket bound at", port)

s.listen(7)
print("Waiting for Clients..")

while True:
    c, addr = s.accept();
    name = c.recv(1024).decode()
    print("Connected to", addr[1] , "named" , name)
    c.send(bytes("Welcome" , 'utf-8'))

    c.close();
