import socket

s = socket.socket()
host = '192.168.5.25'
port = 8080
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from ', addr)
    c.send('Thank you for connecting')
    c.close()
