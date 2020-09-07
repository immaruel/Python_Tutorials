import telepot
import logging # 로그를 찍어주는 라이브러리
from module import get_dir_list # module.py에서 get_dir_list라는 함수 사용
import os
import module



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1348513400:AAEVTzDxNJ-gPeLp5o6W7S-o84Y_O6doy50"


def handler(msg):
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    
    print(msg)
    if content_type == "text":
        #bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))

        # 1. 봇 소통 코드 작성
        str_message = msg["text"]
        if str_message[0:1] == "/": # 맨처음 글자가 '/' (명령어)인경우
            args = str_message.split(" ")
            command = args[0] #  앞 명령어 부분 '/ex' 삭제하고 뒷 부분만 남게함
            del args[0]

            if command == "/dir" or command == "/목록":
                filepath = " ".join(args) # 리스트를 문자열로 바꾸기
                if filepath.strip == ():
                    bot.sendMessage(chat_id,"/dir [대상폴더]를 입력하세요")
                else:
                    # 3. 다시 함수로 받아주기
                    filelist= module.get_dir_list(filepath)
                    bot.sendMessage(chat_id,filelist)
            
            # 5-2 날씨를 불어오기 위한 명령코드 작성
            elif command == "/weather" or command == "/날씨":
                w = " ".join(args) # 리스트를 문자열로 바꾸기
                weather =module.get_weather(w)
                bot.sendMessage(chat_id,weather)

            # 6-3 환율정보를 불어오기 위한 명령코드 작성
            elif command == "/money":
                w = " ".join(args) # 리스트를 문자열로 바꾸기
                output = weather =module.money_translate(w)
                bot.sendMessage(chat_id,output)            

            # 4. 파일 전송기능 만들기
            elif command[0:4] == "/get": # 0~4글자가 get으로 시작하는 경우
                filepath = " ".join(args) # 리스트를 문자열로 바꾸기
                if os.path.exists(filepath): # 파일이 존재하는 경우만 전송
                    try: # 혹시 모를 오류 방지
                        if command == "/getfile":
                            bot.sendDocument(chat_id, open(filepath,"rb"))
                        elif command == "/getimage":
                            bot.sendPhote(chat_id, open(filepath,"rb"))
                        elif command == "/getaudio":
                            bot.sendAudio(chat_id, open(filepath,"rb"))
                        elif command == "/getvideo":
                            bot.sendVideo(chat_id, open(filepath,"rb"))
                    except Exception as e:
                        bot.sendMessage(chat_id, "파일이 전송 실패 {}".format(e))
                else:
                    bot.sendMessage(chat_id, "파일이 존재하지 않습니다.")






bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)
