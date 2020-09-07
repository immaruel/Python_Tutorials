import tkinter
import socket
from threading import Thread



IP = ""
PORT = 0


def recv_message(sock):
    while True: # 메세지 계속받기
        msg = sock.recv(1024)  # 1024byte 받기
        chat_list.insert(tkinter.END,msg.decode())
        chat_list.see(tkinter.END) # 맨마지막으로 보내기
        #print(msg.decode()) # 채팅 소켓으로 넘어온 메세지는 byte로 넘어오므로 디코딩

def connect(event=None): # 버튼을 누르는 것들은 event를 삽입해야함
    global IP, PORT
    connect_string = input_string.get()# 주소 가져오기
    addr = connect_string.split(":")# ip와 port 분리하기
    IP = addr[0]
    PORT = int(addr[1])
    w_connect.destroy() # 사용자가 주소까지 입력하고 버튼을 누르면 사라지게하기


def send_message(event=None):
    input_msg.get()
    sock.send(msg.encode())
    input_msg.set("") # 대화 내용초기화
    if msg == "/bye":
        sock.close()
        window.quit()
    pass



w_connect = tkinter.Tk()

# 1. 기본 주소창 및 버튼 만들기
w_connect.title("접속대상")
tkinter.Label(w_connect, text="접속대상").grid(row=0, column=0) # 화면에 표시될 내용/ grid함수-> 화면내 위치 지정
input_string = tkinter.StringVar(value="127.0.0.1:12000")
input_addr = tkinter.Entry(w_connect, textvariable = input_string, width =20) # w_connect = 부모
input_addr.grid(row=0, column=1) # grid로 위치 지정
c_button = tkinter.Button(w_connect, text="접속하기",command=connect) # 버튼생성
c_button.grid(row=0, column=2, padx=5, pady=5)  # grid로 위치 지정 + 여백주기

# 2. 코드로 진행했을떄 유저화면 정중앙으로 팝업뜨게 하기 
width = 350
height = 50

screen_width = w_connect.winfo_screenwidth()
screen_height = w_connect.winfo_screenheight()

# 2-1. 화면 비율 구하기
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height /2))

w_connect.geometry('{}x{}+{}+{}'.format(width,height,x,y))
w_connect.mainloop()


# 3. 채팅 입력한 창 만들기
window = tkinter.Tk()
window.title("클라이언트")


# 3-2 채팅이 나올 공간 만들기(with 스크롤)
frame = tkinter.Frame(window)
scroll = tkinter.Scrollbar(frame)# 스크롤바 만들기
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

chat_list= tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scroll.set)
chat_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady =5)
frame.pack()


# 3-1 채팅 메세지 받기
input_msg = tkinter.StringVar()
inputbox = tkinter.Entry(window, textvariable=input_msg)
inputbox.bind("<Return>", send_message) # Return 버튼을 누르면 다른 화면으로 이동
inputbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES, padx=5, pady=5) # 팩함수를 이용해 화면배율정하기
send_button = tkinter.Button(window, text="전송",command=send_message) # '전송'버튼 만들기
send_button.pack(side=tkinter.RIGHT, fill=tkinter.X, padx=5, pady=5)




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))

th = Thread(target=recv_message,args=(sock,)) # Thread함수에 args를 튜플형태로 넘기기
th.daemon = True
th.start()

window.mainloop()


