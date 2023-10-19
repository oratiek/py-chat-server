import socket

IP = ""
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.bind((IP, PORT))

sock.listen()
while True:
    client, addr = sock.accept()
    print(addr)
