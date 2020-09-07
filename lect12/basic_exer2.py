from PIL import Image
import requests

'''
0. pillow 다루기 -> RGB사용, 출력 시 width:height
'''

#1. 내 컴퓨터상에 있는 이미지 가져오기
img = Image.open("c:\\test\\sample.jpg")

print(img.size)
img = img.rotate(45)
img.show()
img.save("sample.gif")

#2. 웹 상 이미지 가져오기
url = "https://cdn.pixabay.com/photo/2020/08/12/09/21/sunflowers-5482116__340.jpg"
img = Image.open(requests.get(url, stream=True).raw) # 스트림 형태로 읽은 raw데이터를 열기
img.save("girl.gif")

'''
1. openCV 다루기 -> BGR 사용, 출력시 height:width
'''
import cv2
import requests
import numpy

# 1. 내 컴퓨터 상 이미지 가져오기
img = cv2.imread("exer.jpg", cv2.IMREAD_COLOR) # IMREAD_COLOR로 해당 파일을 읽겠다
print(img.shape)
cv2.imshow("B",img) # 'B'라는 자체 창 이름을가진 뷰어로 열기
cv2.waitKey(0) # 다른 키입력전 까지 무한대로 화면에 뷰어 떠있게 하기
cv2.destroyAllWindows() # 다른 키를 입력하면 창 꺼지게 하기

# 2. 웹 상 이미지 가져오기
url = "https://cdn.pixabay.com/photo/2020/04/12/08/50/child-5033381__340.jpg"
arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8) # 부호가 없는 8비트 정수형 타입으로 numpy 배열 생성
img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
cv2.imshow("C",img)
cv2.waitKey(0) # 다른 키입력전 까지 무한대로 화면에 뷰어 떠있게 하기
cv2.destroyAllWindows() # 다른 키를 입력하면 창 꺼지게 하기

'''
3. pillow와 openCV 호환하여 사용하기
'''

import cv2
import requests
import numpy
from PIL import Image

pil_image = Image.open("sample.png")
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

cv2.imshow("D",opencv_image)
cv2.waitKey(0) # 다른 키입력전 까지 무한대로 화면에 뷰어 떠있게 하기
cv2.destroyAllWindows() # 다른 키를 입력하면 창 꺼지게 하기