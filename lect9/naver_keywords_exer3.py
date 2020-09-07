import requests
from bs4 import BeautifulSoup
import time
# json = requests.get('https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=4&ma=2&si=2&en=2&sp=2').json()

# ranks = json.get("data")

# for r in ranks:
#     rank = r.get("rank")
#     keyword = r.get("keyword")
#     print(rank, keyword)


lists = bs.find_all("li",{"class":"ah_item"})
for li in lists:
    title = li.find("span",{"class":"ah_k"}).text
    print(title)

lists = bs.select("li.ah_item")
for li in lists:
    title = li.select("span.ah_k")[0].text
    print(title)