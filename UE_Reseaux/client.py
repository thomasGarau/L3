# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("Saisisser votre message")
    #message = list(message.encode("ascii"))
    s.sendall(message.encode())
    data = s.recv(1024).decode()
print('Received', repr(data))
a