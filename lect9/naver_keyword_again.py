import requests
from bs4 import BeautifulSoup

def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper

@time_function
def r_select(url,parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li",{"class":"realtime_item"})

    titles = []
    for li in lists:
        title = li.select("a > span > strong.rank")[0].text 
        titles.append(title)
    return titles

url = "https://www.naver.com"
r_find_all(url, "html.parser")
r_select(url, "html.parser")

r_find_all(url, "lxml")
r_select(url, "lxml")



r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.text, "lxml")

#lists = bs.find_all("li",{"class":"realtime_item"})

# for li in lists:
#     print(li)
#     title = li.find("strong",{"class":"rank"}).text
#     story = li.find("span",{"class":"keyword"}).text
li.select("a > span > strong.rank")[0].text 
lists = bs.select("li.realtime_item")
for li in lists:
    point =  li.select("a > span > strong.rank")[0].text # select 는 항상 list를 리턴
    print(point)