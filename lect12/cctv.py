'''
웹캠으로 CCTV 만들기 
openCV는 height x width
'''
import cv2
import numpy as np
from skimage.measure import compare_ssim
from PIL import Image, ImageFont, ImageDraw


cap = cv2.VideoCapture(0) 
if cap.isOpened() == False: # 카메라캠이 안켜진 경우
    print("카메라를 오픈 할 수 없습니다.")

frame_width =int(cap.get(3))
frame_height =int(cap.get(4))

old_image = None # 이전 이미지
show_image = None

while True:
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
                
        old_image = frame # 현재 이미지를 대입
        cv2.imshow("CCTV",show_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()