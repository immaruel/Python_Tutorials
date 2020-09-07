import socket
from threading import Thread

def recv_message(sock):
    while True: # 메세지 계속받기
        msg = sock.recv(1024)  # 1024byte 받기
        print(msg.decode()) # 채팅 소켓으로 넘어온 메세지는 byte로 넘어오므로 디코딩

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",12000))

th = Thread(target=recv_message,args=(sock,)) # Thread함수에 args를 튜플형태로 넘기기
th.daemon = True
th.start()


while True: # 입력 계속받기
    msg = input("입력:  ")
    sock.send(msg.encode()) # 보낼 메세지를 문자열 형태를 byte로 인코딩해서 보냄

    if msg == "/bye":
        break
sock.close()
