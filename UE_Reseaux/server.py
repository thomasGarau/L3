# Echo server program
import socket
from datetime import date

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            else:
                message = data.decode().split(' ', 1)
                if message[0] == "upper":
                    conn.sendall(message[1].upper().encode())
                elif message[0] == "lower":
                    conn.sendall(message[1].lower().encode())
                elif message[0] == "datenow":
                    conn.sendall(str(date.today()).encode())
                else : 
                    conn.sendall("erreur".encode())