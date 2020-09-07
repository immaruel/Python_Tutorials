# '''
# 0. pillow 사용 -> RGB사용, 출력시 width x height
# '''
# from PIL import Image
# import requests

# # 1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
# img = Image.open("c:\\test\\sample.jpg") # Image함수를 이용하여 로컬폴더내 파일열기
# #img.show()
# print(img.size)
# img = img.rotate(70)
# img.save("sample.png")

# # 2. 웹 상 이미지 가져오기
# url = "https://cdn.pixabay.com/photo/2020/05/13/17/38/foliage-5168308__340.jpg"
# img = Image.open(requests.get(url, stream=True).raw)
# img.save("apple.png")

# '''
# 1. openCV 다루기 -> BGR 사용, 출력시 height x width
# '''
# import cv2
# import requests
# import numpy # 고성능 연산을 위한 라이브러리

# #1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
# img = cv2.imread("sample.jpg", cv2.IMREAD_COLOR) # IMREAD_COLOR 으로 읽겠다
# print(img.shape) # 출력시 세로:340, 가로:510, _ 으로 출력
# cv2.imshow("bb",img) # 'bb'라는 자체 창이읆을 가진 뷰어로 열기
# cv2.waitKey(0) # 다른 키 입력전까지 무한대로 뷰어를 화면에 띄어놓기
# cv2.destroyAllWindows() # 해당 키를 입력하면 창 꺼지게 하기

'''
3. pillow와 openCV 호환하여 사용하기
'''
import cv2
import requests
import numpy
from PIL import Image


pil_image = Image.open("apple.png")
opencv_image = numpy.array(pil_image) # pillow 이미지를 openCV이미지로 변경
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR) # 상호간에 특징 호환

cv2.imshow("aa", opencv_image) # 뷰어로 열기
cv2.waitKey(0) # 다른 키 입력전까지 무한대로 뷰어를 화면에 띄어놓기
cv2.destroyAllWindows() # 해당 키를 입력하면 창 꺼지게 하기

