import socket

IP = "100.75.59.39"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))
welcome_msg = sock.recv(1024)
print(welcome_msg.decode("utf-8"))
while True:
    send = input(">")
    sock.send(send.encode("utf-8"))
    recv = sock.recv(1024)
    print(recv.decode("utf-8"))

