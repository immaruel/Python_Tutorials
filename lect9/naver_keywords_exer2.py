import requests
from bs4 import BeautifulSoup
import pprint

json = requests.get('https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=20s&gr=4&ma=2&si=2&en=2&sp=2').json()

ranks = json.get("data")
a = pprint.pprint(ranks)
print(a)

for r in ranks:
    rank = r.get("rank")
    keyword = r.get("keyword")
    print(rank, keyword)