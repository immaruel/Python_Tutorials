'''
웹캠으로 CCTV 만들기 
openCV는 height x width
'''
import cv2
import numpy as np # 배열 라이브러리
from skimage.measure import compare_ssim # 이미지 유사도 측정 라이브러리
from PIL import Image, ImageFont, ImageDraw # pillow 라이브러리 (openCV와의 호환을 위해 별도 코드 추가해야함)


#1. 웹캠 열기
cap = cv2.VideoCapture(0) # '0'번은 사용자 컴퓨터의 디바이스 번호, 0번째:가장 처음에 해당하는 디바이스
if cap.isOpened() == False:
    print("카메라 오픈 불가합니다!")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#2. 유사도 
old_image = None # 이전 이미지(몇초전) 변수설정
show_image = None

#1.1
while True:
    ret, frame = cap.read() # ret:성공여부, frame:현재 캡처된 웹캠이미지
    if ret == True:
        if old_image is not None: # 비교할 이전 이미지가 생성되었다면

            show_image = frame.copy()  # 현재 보이는 이미지(원본)을 다른 변수로 설정한 변수에 대입
        
            grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 현재 보이는 이미지 흑백으로 바꾸기
            grayB = cv2.cvtColor(old_image, cv2.COLOR_BGR2GRAY) # 이전 이미지(몇초전) 흑백으로 바꾸기
            (score, diff) = compare_ssim(grayA, grayB, full=True) #score: 1.0미만의 유사도확률, diff: 유사도를 측정한 후 이미지
            diff = (diff * 255).astype("uint8")
            #cv2.imshow("DIFF",old_image) # 이전(몇초전) 이미지 출력
            cv2.imshow("DIFF",diff) # 흑백으로 바꾼 이미지 출력
            print("SSIM :{}".format(score))
            

            #3. 웹캠 영상 하단 문장 출력시키기
            text = "유사도 : {:0.9f}".format(score)
            font = ImageFont.truetype("malgun.ttf",17)

            text_w, text_h = font.getsize(text) # 영상에 텍스트가 위치 설정하기
            w = show_image.shape[1] # shape[1]는 width에 해당
            h = show_image.shape[0] # shape[0]는 height에 해당
            X_POS = w - text_w - 10
            Y_POS = h - text_h - 10

            pil_image = Image.fromarray(show_image) # openCV이미지를 pillow이미지로 변경
            draw = ImageDraw.Draw(pil_image)
            draw.text((X_POS, Y_POS), text, (2552,255,255), font=font) # 해당위치, 해당텍스트, 해당텍스트색깔, 해당텍스트글씨체
            show_image = np.array(pil_image) # pillow이미지를 openCV이미지로 변경


            if score < 0.90:
                cv2.rectangle(show_image,  (0,0), (w,h), (0,0,255), 6)

        old_image = frame # 현재 이미지를 대입
        cv2.imshow("CCTV",show_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()