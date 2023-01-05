import struct
import time
import socket
import thread

HOST = 'localhost' 
PORT = 50007         

def encode_message(stru: str) -> bytes:
    temps = time.time() *1000
    a = len(stru)
    stru = stru.encode()
    taille = len(stru) + len(str(temps).encode())
    return (struct.pack(">I", taille), struct.pack(f">f{a}s", temps, stru))


def decode_message(b: bytes) -> str:
    return struct.unpack(f">If{len(b)}s",b)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = input("Veuillez saisir un message")
    encodeTaille, encodeMessage = encode_message(data)
    s.sendall(encode_message(encodeTaille))
    s.sendall(encode_message(encode_message))
    display = s.recv(decode_message(encodeTaille))
    print(display)
