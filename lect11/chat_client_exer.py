import socket
from threading import Thread

def recv_message(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",12000))

th = Thread(target=recv_message, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = input("입력: ")
    sock.send(msg.encode()) # 메세지를 보낼 떄 문자열 형태를 byye로 인코딩 해서 보내기

    if msg == '/bye':
        break
sock.close()