import socket


IP = ""
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP,PORT))
sock.listen()
while True:
    client, addr = sock.accept()
    client.send(b"welcome to chat server")
    break

while True:
    recv = client.recv(1024) 
    print(recv.decode("utf-8"))
    send = input(">")
    client.send(send.encode("utf-8"))

