import socket

HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    nbEssaie = s.recv(1024).decode()
    nbEssaie = int(nbEssaie)
    intervale = s.recv(1024).decode()
    i = 0
    trouvee = False

    print("intervale: ", intervale,  "nbEssaie", nbEssaie)
    while i < nbEssaie and not trouvee :
        message = input("Saisisser un nombre")
        try:
            message = int(message)
        except:
            print("erreur veuillez saisir un nombre")
            continue
        
        s.sendall(str(message).encode())
        i+=1
        reponse = s.recv(1024).decode()
        print(reponse)
        if reponse == "Felicitation":
            trouvee = True
