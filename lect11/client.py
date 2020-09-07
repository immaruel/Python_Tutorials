'''
서버역할
1. 소켓 생성 
2.
3. 접속시도
4. 
5. 데이터 송수신 # 소켓통신은 문자열 형태가 아닌 byte형태
6. 접속종료
'''

import socket
print("1.소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 통신

print("3. 접속시도")
sock.connect(("127.0.0.1", 12000))

print("5. 데이터 송수신")
sock.sendall("hello socket programming".encode()) 

print("6. 접속종료")
sock.close()