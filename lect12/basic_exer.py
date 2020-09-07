'''
0. pillow 다루기 - > RGB사용, 출력시 width:height
'''

from PIL import Image
import requests

# 1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
img = Image.open("c:\\test\\mix.jpg")
#img.show()
img = img.rotate(75).show()
#img.save("mix.png")

# 2. 웹 상 이미지 가져오기 및 수정
url = "https://cdn.pixabay.com/photo/2020/06/10/09/25/anemone-5281964__340.jpg"
img = Image.open(requests.get(url, stream=True).raw)
img.save("exer.jpg")

'''
1. openCV 다루기 -> RGB 사용, 출력시 height:width 
'''
import cv2
import requests
import numpy # 고성능 연산을 위한 라이브러리

# 1. 내 컴퓨터 폴더에 있는 이미지 가져오기 및 수정
img = cv2.imread("exer.jpg", cv2.IMREAD_COLOR)
print(img.shape)
cv2.imshow("bb",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 웹 상 이미지 가져오기
url = "https://cdn.pixabay.com/photo/2019/09/23/16/39/square-4499056__340.jpg"
arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8)
img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

cv2.imshow("cc",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
3. pillow와 openCV 호환하여 사용하기
'''
import cv2
import requests
import numpy
from PIL import Image

pil_image = Image.open("exer.jpg")
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

cv2.imshow("smaple", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()