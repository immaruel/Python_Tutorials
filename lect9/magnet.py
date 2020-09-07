import requests
from bs4 import BeautifulSoup
import re # 정규식 라이브러리

# 1. 구글 검색 페이지 받아오기
"리눅스 magnet:?xt="

def search_google(keyword,start_page,end_page=None):
    #keyword = "리눅스"
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D&start={1}".format(keyword,keyword)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}

    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div.rc > div.r > a")
    #print(divs)

    results = []
    if end_page is None:
        counts = bs.select("div#result-stats")[0].text.replace("검색결과 약", "").replace("개", "").replace(",", "").split("(")[0].strip()
        end_page = int(int(counts) / 10)
        if end_page > 20: # 2페이지에 해당
            end_page = 20 # 2페이지에 고정시키기

        #print(counts)

#search_google("리눅스",1)

    # for div in divs:
    #     pr = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div.rc > div.r > a")
    #     print("*"*60)

    for a in links:
        #print(a["href"])
        href = a["href"]
        text = a.select("h3")
        #title = a.text
        #print(title)
        if len(text) <= 0:
            continue
        title = text[0].text

        try:
            # 2. 해당 페이지 접속하여 받아오기
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))# select함수 대신 전체 주소에서 마그넷 주소를 찾아야 되기 때문에 정규식 사용

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                print(title,magnet)
                results.append((title,magnet))
        except:
            pass
    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword,start_page,end_page=end_page))

    return results
results = search_google("리눅스",0) # 0은 첫페이지에 해당

for r in results:
    print(r)

