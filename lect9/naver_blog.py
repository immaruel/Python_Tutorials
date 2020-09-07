import requests
from bs4 import BeautifulSoup

# 크롤링코드 함수로 만들기

def get_search_naver_blog(query, start_page=1, end_page=None): # 네이버 블로그 페이지 :1=11, 2=11, 3=21, 4=31
    # 11 = (2 - 1) * 10 + 1
    # 21 = (3 - 1) * 10 + 1
    start = (start_page - 1) * 10 + 1
    url = "https://search.naver.com/search.naver?query={}&start={}".format(query, start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    result = []
    if end_page is None:
        # 11-20 / 8,422건
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace(",","").strip())
        # 8,422건
        # tot_counts = tot_counts.split("/")[-1]  # 8,422건 만 받아오기
        # tot_counts.replace("건","").replace(",","").strip() # "건"",",공백 지우기 -> '8422'만 남음
        end_page = tot_counts / 10

        if end_page > 900:
            end_page = 900 # 끝나는 페이지가 900이상되면 900으로 고정
        
    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try: # 혹시 모를 오류 방지하기 위해 try-except 구문사용
            #print(li)
            thumbnail = li.select("img")[0]["src"] # img 태그의 src값만 가져오기
            title = li.select("dl > dt > a")[0]
            summary = li.select("dl > dd.sh_blog_passage")[0].text

            # title에 해당하는 정보 나눠 출력하기
            title_link = title["href"]
            title_text = title.text

            result.append((thumbnail, title_text, title_link, summary)) # 튜플형태로 리스트에 추가
        except:
            continue

    if start_page < end_page:
        start_page += 1
        result.extend(get_search_naver_blog(query, start_page=start_page, end_page=end_page)) #get_search_naver_blog함수를 재귀함수로 반복
    return result

results = get_search_naver_blog("파이썬강좌",start_page=1,end_page=3)

for i in results:
    print(i)
    


# 크롤링 코드
query = "파이썬 강좌"
url = "https://search.naver.com/search.naver?query={}".format(query)

r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")

lis = bs.select("li.sh_blog_top")
for li in lis:
    #print(li)
    thumbnail = li.select("img")[0]["src"] # img 태그의 src값만 가져오기
    title = li.select("dl > dt > a")[0]
    summary = li.select("dl > dd.sh_blog_passage")[0].text

    # title에 해당하는 정보 나눠 출력하기
    title_link = title["href"]
    title_text = title.text
