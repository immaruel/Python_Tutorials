'''
서버역할
1. 소켓 생성 
2. 바인딩 # 이 IP와 PORT를 사용할 것이다
3. 접속대기
4. 접속 수락
5. 데이터 송수신
6. 접속종료
'''

import socket
print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 통신

print("2. 바인딩")
sock.bind(("",12000))

print("3. 접속대기")
sock.listen()

print("4. 접속 수락")
c_sock, addr = sock.accept()

print("5. 데이터 송수신")
receive_data = c_sock.recv(1024)
print("수신된 데이터 : {}".format(receive_data))

print("6. 접속종료")
c_sock.close() # 클라이언트 소켓 종료
sock.close()   # listen 소켓 종료