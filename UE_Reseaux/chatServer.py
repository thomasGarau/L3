import struct
import time
import socket
import selectors

HOST = 'localhost'
PORT = 50007     
sel = selectors.DefaultSelector()
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(100)
sock.setblocking(False)
list_client = []

def encode_message(stru: str) -> bytes:
    temps = time.time() *1000
    a = len(stru)
    stru = stru.encode()
    taille = len(stru) + len(str(temps).encode())
    return struct.pack(f">If{a}s",taille, temps, stru)

def decode_message(b: bytes) -> str:
    a = len(b) -8
    return struct.unpack(f">If{a}s",b)


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
    
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)





