'''
웹캠으로 CCTV 만들기
openCV는 height x width
'''

import cv2
import numpy as np # 배열 라이브러리
from skimage.measure import compare_ssim # 이미지 유사도 측정 라이브러리 및 함수
from PIL import Image, ImageFont, ImageDraw # pillow 라이브러리 (openCV라이브러리와 혼용 시 별도 호환코드 작성 필요)

# 1. 웹캠 켜기
cap = cv2.VideoCapture(0) # 사용자 디바이스에서 첫번째에 해당하는 '0'번 디바이스 사용
if cap.isOpened() == False: # 캠이 켜지지 않았다면
    print("카메라 오픈 불가합니다!")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

old_image = None # 방금전 이미지 변수설정
show_image = None
while True:  # 무한루프
    ret, frame = cap.read() # ret: 성공여부, frame: 현재 보이는 웹캠 이미지
    if ret == True:
        if old_image is not None: # 방금전 이미지가 몇 초전에 생성되었다면
            
            show_image = frame.copy()

            grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 현재 이미지를 흑백으로 변경
            grayB = cv2.cvtColor(old_image, cv2.COLOR_BGR2GRAY) # 몇초전 이미지를 흑백으로 변경
            (score, diff) = compare_ssim(grayA, grayB, full=True) # score: 1.0미만의 유사도확률, diff: 유사도를 측정한 몇초후 이미지
            diff = (diff * 255).astype("uint8")
            cv2.imshow("DIFF", diff) # 흑백으로 바꾼 몇초전 이미지
            print("SSIM:{}".format(score)) # 유사도 출력하기


            # 3. 웹캠 영상 하단 문장에 출력시키기
            text = "유사도: {:0.f}".format(score)
            font = ImageFont.truetype("malgun.ttf",24)

            text_w, text_h = font.getsize(text) # 영상에 표시될 텍스트 위치 설정
            w =show_image.shape[1]
            h =show_image.shape[0]
            X_POS = w - text_w - 10
            Y_POS = h - text_h - 10

            pil_image = Image.fromarray(show_image) # openCV이미지를 pillow이미지로 변경
            draw = ImageDraw(pil_image)
            draw.text((X_POS, Y_POS), text, (2552,255,255), font=font) # 해당위치, 해당텍스트, 해당텍스트색깔, 해당텍스트글씨체
            show_image = np.array(pil_image) # pillow이미지를 openCV이미지로 변경

            if score < 0.90: # 유사도가 일정이하로 떨어질경우
                cv2.rectangle(show_image,  (0,0), (w,h), (0,0,255), 6)


        old_image = frame #  현재이미지를 대입
        cv2.imshow("CCTV",frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()