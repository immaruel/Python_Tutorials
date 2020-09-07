import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.text,"lxml")

lists = bs.select("li.realtime_item")
print(lists)
# for li in lists:
#     point = li.selcet("a > span.keyword")
#     print(point)