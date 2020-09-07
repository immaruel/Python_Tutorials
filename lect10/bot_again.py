import telepot # 텔레그램 소통 라이브러리
import logging # 로그를 찍어주는 라이브러리
import os
from module import get_dir_list # 다른 파이썬 파일에서 함수 가져오기
import module

# 2. 로그찍기
logging.basicConfig(level=logging.DEBUG) # 어느 수준의 로그를 찍을것인가?
logger = logging.getLogger(__name__) # 로그이름을 파일명으로 설정


TELEGRAM_TOKEN = "1091208987:AAEciNrpDbpSHjnwecI0IkpjsnyI4fxARts"


def handler(msg):
    # 1-2. 기본적인 handler 함수에 들어가야 할 내용
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True) 

    print(msg)
    if content_type == 'text':
        #bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))
        str_message = msg["text"]
        if str_message[0:1] == "/": # 채팅으로 입력되는 글자가 '/'로 시작할때
            args = str_message.split(" ") # 예를들어 '/dir c:\\test'로 입력할때 '/dir'과 'c:\\test'사이를 띄게 입력한것을 인지시키기 
            command = args[0]
            del args[0] # '/dir' 삭제

            #1-3 명렁어별 기능 

            # 1-3-1 파일 목록을 구해주는 함수
            if command == "/dir":
                filepath = "".join(args) # args를 리스트형태가 아닌 문자열 형태로 변환
                if filepath.strip() == "": # 뒤에 아무 정보 없이 '/dir'만 입력된경우
                    bot.sendMessage(chat_id, "/dir [대상폴더]로 입력해주세요")
                else:
                    # 1-3-3 해당함수 호출
                    filelist = module.get_dir_list(filepath) # 인자값으로 어느 폴더를 줄지 결정 -> args
                    bot.sendMessage(chat_id, filelist)

            #2-1 날씨 구하는 함수 실행시키기
            elif command == "/weather":
                w = "".join(args) # args를 리스트형태가 아닌 문자열 형태로 변환
                weather = module.get_weather(w)
                bot.sendMessage(chat_id, weather)

            
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




#1-1. Telegram 토큰 설정
bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)