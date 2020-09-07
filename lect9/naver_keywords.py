import requests
from bs4 import BeautifulSoup
import time

def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} [} time {}".format(f.__name__,args[1],end_time))
        return result
    return wrapper

def r 
r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.text, "lxml")

# 방법 1
lists = bs.find_all("li", {"class":"ah_item"}) # find_all : 전체 요소 다가져오기
for li in lists:
    title = li.find("span",{"class":"ah_k"}).text # find : 전체 중 맨처음(태그)꺼만 가져오기
    print(title)

# 방법 2 - select함수 사용 -> 항상 리스트를 리턴시킴!!
# lists = bs.select("li.ah_item")
# for li in lists:
#     title = li.select("span.ah_k")[0].text
#     print(title)