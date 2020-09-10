'''
네이버 블로그 검색 결과 크롤링
'''
import requests
from bs4 import BeautifulSoup

def search_naver_blog(query, start_page=1, end_page=None): # 네이버 블로그 페이지
    start = (start_page - 1)*10 + 1
    url ="https://search.naver.com/search.naver?&query={}&start={}".format(query,start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    result = []
    if end_page is None:
        # 검색결과수 및 마지막 페이지 크롤링
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace(",","").strip())
        #print(tot_counts)

        end_page = tot_counts / 10

    if end_page > 900:
        end_page = 900
    
    # 나머지 정보 크롤링
    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try: # 혹시모를 오류 방지를 위해 try 문 사용
            thumbnail = li.select("img")[0]["src"] # img 태그의 src값만 가져오기
            title = li.select("dl > dt > a")[0]
            summary = li.select("dl > dd.sh_blog_passage")[0].text

            # title 정보 나눠 저장
            title_link = title["href"]
            title_text = title.text

            result.append((thumbnail, title_text, title_link, summary)) # 튜플형태로 리스트에 추가

        except:
            continue
    if start_page < end_page:
        start_page += 1
        result.extend(search_naver_blog(query, start_page=start_page, end_page=end_page)) #get_search_naver_blog함수를 재귀함수로 반복
    return result

results = search_naver_blog("파이썬강좌",start_page=1,end_page=4)

for i  in results:
    print(i)
