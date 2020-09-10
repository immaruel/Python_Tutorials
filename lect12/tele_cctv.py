import telepot
import logging # 로그를 찍어주는 라이브러리
from module import get_dir_list # module.py에서 get_dir_list라는 함수 사용
import os
import module

import cv2
import numpy as np
from skimage.measure import compare_ssim
from PIL import Image, ImageFont, ImageDraw

import threading
import time


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1348513400:AAEVTzDxNJ-gPeLp5o6W7S-o84Y_O6doy50"

run_thread = False

def send_frame_to_telegram(chat_id, frame):
    cv2.imwrite("_tmp.jpg",frame)
    bot.sendPhote(chat_id, open("_tmp.jpg", mode="rb"))

def capture_cam(chat_id):
    global run_thread
    cap = cv2.VideoCapture(0) 
    if cap.isOpened() == False: # 카메라캠이 안켜진 경우
        print("카메라를 오픈 할 수 없습니다.")

    frame_width =int(cap.get(3))
    frame_height =int(cap.get(4))

    old_image = None # 이전 이미지
    show_image = None

    while run_thread:
        ret, frame = cap.read() # ret:성공여부, frame:현재 캡처된 웹캠이미지
        if ret == True:
            show_image = frame.copy()
            if old_image is not None:
                grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                grayB = cv2.cvtColor(old_image, cv2.COLOR_BGR2GRAY)
                (score, diff) = compare_ssim(grayA, grayB, full=True) #score: 1.0미만의 유사도확률 diff: 유사도를 측정한 후 이미지
                diff = (diff * 255).astype("uint8")
                cv2.imshow("DIFF",diff)
                #print("SSIM : {}".format(score))
                text = "유사도: {:0.9f}".format(score)

                font = ImageFont.truetype("malgun.ttf", 17)
                text_w, text_h = font.getsize(text)
                w = show_image.shape[1] # shape[1]는 width에 해당
                h = show_image.shape[0] # shape[0]는 height에 해당
                X_POS = w - text_w - 10
                Y_POS = h - text_h - 10

                pil_image = Image.fromarray(show_image)
                draw = ImageDraw.Draw(pil_image)
                draw.text((X_POS, Y_POS), text, (2552,255,255), font=font)
                show_image = np.array(pil_image)

                if score < 0.90:
                    cv2.rectangle(show_image,  (0,0), (w,h), (0,0,255), 6)
                    send_frame_to_telegram(chat_id, show_image)
            old_image = frame # 현재 이미지를 대입
            cv2.imshow("CCTV",show_image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def handler(msg):
    global run_thread
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
            
            #7. cctv 기능 추가하기
            elif command == "/mon":
                if args == "start":
                    if not run_thread:
                        print("감시시작")
                        run_thread = True
                        t = threading.Thread(target=capture_cam, args=(chat_id,))
                        t.daemon = True
                        t.start()
                        bot.sendMessage(chat_id, "감시를 시작했습니다.")
                    else:
                        bot.sendMessage(chat_id, "현재 감시가 동작 중입니다.")
                elif args[0] =="stop":
                    print("감시종료")
                    run_thread = False
                    bot.sendMessage(chat_id, "감시를 중지합니다.")

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
