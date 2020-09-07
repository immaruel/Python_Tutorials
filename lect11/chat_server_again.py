import socketserver

# 1. 기본 소켓 통신 구조 짜기
class MyHandler(socketserver.BaseRequestHandler):
    # 3. 서버에 누가 접속했는지 볼수 있는 기능 추가
    users = {}

    # 4. 다른 현재 참여중인 유저들에게 새로 들어온 유저 알리기 기능 추가
    def send_all_message(self, msg): # class 함수(def)이므로 self를 붙여야함
        for sock, _ in self.users.values():
            sock.send(msg.encode())


    def handle(self):
        print(self.client_address) # client_address는 BaseRequestHandler내에 구현되어 있는 정보

        while True: # 닉네임 중복을 막기 위한 무한루프 실행
            # 2. 유저가 채팅 접속 시 유저의 닉네임 물어보는 기능 추가
            self.request.send("채팅 닉네임을 입력하세요: ".encode())

            nickname = self.request.recv(1024).decode() # 유저가 입력한 닉네임을 받기
            #print(nickname)
            if nickname in self.users:
                self.request.send("이미 등록된 닉네임 입니다. \n".encode())
            else:
                self.users[nickname] = (self.request, self.client_address) # 딕셔너리 형태 -> nickname(keys) / self.request, self.client_address(value)
                print("현재 {}명 참여중".format(len(self.users)))
                
                # 4-1 출력시키는 문장코드
                self.send_all_message("[{}님이 입장했습니다.".format(nickname))
                break

        # 4-2 실제 채팅 주고 받기 무한루프
        while True:
            msg = self.request.recv(1024)
            if msg.decode() == "/bye":
                self.request.close()
                break
            self.send_all_message("[{}] {}".format(nickname, msg.decode()))
        
        # 5. 4-2에서 break되어 나오게 된것은 채팅을 종료 한것이므로 users에서 해당 유저 삭제
        if nickname in self.users:
            del self.users[nickname]
            self.send_all_message("{}님이 퇴장하셨습니다.".format(nickname))
            print("현재 {}명 참여중".format(len(self.users)))

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("", 12000), MyHandler)  # 12000을 포트로 쓰고 MyHandler를 사용
server.serve_forever()
server.shutdown()
server.server_close() # 소켓 닫기
