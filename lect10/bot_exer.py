import telepot
import logging
import os
from module import get_dir_list
import module

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1348513400:AAEVTzDxNJ-gPeLp5o6W7S-o84Y_O6doy50"

def handler(msg):
    content_type, chat_type, chat_id, ms_date, ms_id = telepot.glance(msg, long=True)
    #bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))

    # 봇 소통 코드 작성
    str_message = msg["text"]
    if str_message[0:1]  == "/": # 맨처음 글자가 '/'(명령어)로 시작하는 경우
        args =str_message.split(" ")
        command = args[0] # 앞 명령어 부분('/ex')를 삭제하게 뒷 부분만 남게함
        del args[0]

        if command == "/dir" or command == "/목록":
            filepath = " ".join(args) # 리스트를 문자열로 바꾸기
            if filepath.strip == ():
                bot.sendMessage(chat_id, "/dir [대상폴더]를 입력하세요")
            else: #조건을 만족하지 못할시 다시 함수로 받아주기
                filelist = module.get_dir_list(filepath)
                bot.sendMessage(chat_id, filelist)



        # 파일 전송 기능 만들기
        elif command[0:4] == "/get": # 0~4글자가 get으로 시작하는 경우
            filepath = " ".join(args) # 리스트를 문자열로 바꾸기
            if os.path.exists(filepath): # 파일일 존재하는 경우만 전송
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
                    bot.sendMessage(chat_id, "파일 전송실패 {}".format(e))
            else:
                bot.sendMessage(chat_id, "파일 존재하지 않네요")





                

bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)

