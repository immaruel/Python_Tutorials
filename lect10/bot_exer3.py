import telepot #텔레그램 소통 라이브러리
import logging # 로그를 찍어주는 라이브러리
import os


TELEGRAM_TOKEN = "1190901796:AAH_2Oz66YGyMfzZq4OoSxC1lHzGQoQhKHE"


#1-3-2 파일목록을 구해오는 함수
def get_dir_list(dir): # 목록을 인자로 받음
    str_list = "" # 문자열 형태 한개 변수 설정
    if os.path.exists(dir): # 해당 입력한 인자(폴더)가 존재하는지 확인
        file_list = os.listdir(dir) # 파일목록을 구해서 대입
        file_list.sort() # 파일목록정렬
        for f in file_list:
            full_path = os.path.join(dir,f) # 전체 경로 설정
            if os.path.isdir(full_path):
                f = "[" + f + "]" # 폴더인 경우 폴더명 가로로 감싸주기
            str_list += f
            str_list += "\n"
        str_list.strip() # 공백제거
    return str_list



def handler(msg):# 인자로 메세지 받기
    #1-2 기본적인 handler 함수에 들어가야할 내용
    content_type, chat_type, chat_id,msg_id = telepot.glance(msg, long=True)

    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #bot.sendMessage(chat_id,"[반사] {}".format(msg['text']))
        str_message = msg["text"]
        if str_message[0:1] == "/": # 채팅으로 입력되는 글자가 '/'로 시작될때
            args = str_message.split(" ") # 예를들어 사용자가 '/dir c:\\test'로 입력할때 '/dir' 'c:\\test'를 띄게 입력한것을 인지시키기
            command = args[0] # '/dir'일때
            del args[0] # '/dir' 삭제

            #1-3 명령어별 기능

            #1-3-1 파일목록을 구해주는 함수
            if command == "/dir":
                filepath ="".join(args) #args를 리스트 형태가 아닌 문자열 형태로 변환
                if filepath.strip() == "": # 공백을 제거했을 때 뒤에 아무정보 없이 그냥 '/dir'만 입력된경우
                    bot.sendMessage(chat_id, "/dir [대상폴더]로 입력해주세용")
                else: 
                    #1-3-3 해당함수 호출
                    filelist = get_dir_list(filepath) #인자값으로 어느 폴더를 줄지 선택
                    bot.sendMessage(chat_id,filelist)

            
            #1-3-3 파일 전송해주기
            elif command[0:4] == "/get": # 0~4번째 글자가 '/get'인 경우
                filepath = "".join(args) # args를 리스트형태가 아닌 문자열 형태로 변환
                if os.path.exists(filepath): # 파일이 존재하는 경우만 전송하기
                    try: # 혹시 모를 오류 대비
                        if command == "getfile":
                            bot.sendDocument(chat_id, open(filepath, "rb")) # 문서파일 오픈해서 전송하기
                        elif command == "/getimage":
                            bot.sendPhoto(chat_id, open(filepath, "rb")) # 사진파일 오픈해서 전송하기
                        elif command == "/getaudio":
                            bot.sendAudio(chat_id, open(filepath, "rb")) # 오디오파일 오픈해서 전송하기
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(filepath, "rb")) # 동영상파일 오픈해서 전송하기
                    except Exception as e:
                        bot.sendVideo(chat_id, "파일전송실패".format(e))
                else: # 파일이 목록에 없는경우
                    bot.sendMessage(chat_id,"파일존재 하지 않네용")














#1-1 Telegram 토큰 설정
bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)

