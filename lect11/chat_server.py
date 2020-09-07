import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users = {}
    
    # 접속한 나머지 유저들에게 새로 접속한 사람 알려주는 함수만들기
    def send_all_message(self.msg):
        for sock, _ in self.values():
            sock.send(msg.encode())

    def handle(self):
        print(self.client_address) # client_address는 BaseRequestHandler에 구현된 정보
        while True: # 닉네임이 중복되지 않을 떄까지 무한루프 돌기
            self.request.send("채팅 닉네임을 입력하세요:".encode())
            nickname = self.request.recv(1024).decode()
            #print(nickname)
            if nickname in self.users:
                self.request.send("이미 등록된 닉네임입니다.\n".encode())
            else:
                self.users[nickname] = (self.request, self.client_address) # 튜플형태
                print("현재 {}명 참여중".format(len(self.users)))

                self.send_all_message("[{}님이 입장했습니다".format(nickname))
                break
        while True:
            msg = self.request.recv(1024)
            if msg.decode() == "/bye":
                self.request.close()
                break
            self.send_all_message("[{} [}".format(nickname, msg.decode()))
        
        if nickname in self.users:
            del self.users[nickname]
            self.send_all_message("[{}님이 퇴장하셨습니다.".format(nickname))
            print("현재 {}명 창여중".format(len(users)))

                
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server =ChatServer(("",12000),MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()

