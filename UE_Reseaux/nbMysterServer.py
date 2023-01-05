import random
import socket


HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
nbEssaie = 7
intervale = (0,100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    mystere = random.randint(0,101)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        conn.sendall(str(nbEssaie).encode())
        conn.sendall(str(intervale).encode())
        i = 0
        trouvee = False

        while i < nbEssaie and not trouvee:
            data = conn.recv(1024).decode()
            data = int(data)
            if data == mystere:
                retour = "Felicitation"
                trouvee = True
            elif data > mystere:
                retour = "Faux c'est moins"
            else:
                retour = "Faux c'est plus"
            i +=1
            conn.sendall(retour.encode())
    
