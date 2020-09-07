import requests
from bs4 import BeautifulSoup
import pandas

def get_movie_point(start, end=1): # end 디폴트를 1로 설정
    results = []
    for i in range(start, end+1):
        url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}".format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        trs = bs.select("table.list_netizen > tbody > tr")
        for tr in trs:
            # 번호
            number = tr.select_one("td.ac.num").text
            # 작성자
            writer = tr.select_one("td.num > a.author").text

            # 타이틀
            tr_data = tr.select_one("td.title")
            # 타이틀 중 제목만 추출
            title = tr_data.select_one("a").text
            # 타이틀 중 점수만 추출
            point = tr_data.select_one("div.list_netizen_score > em").text

            
            #print(number,writer,title,point)

            content = tr_data.text.strip()
            results.append({
                "number": number,
                "point": point,
                "writer": writer,
                "content": content,
                "title":title
            })
    return results
#print(get_movie_point(1,3))

column = ["영화제목","점수","작성자","작성자번호"] # 엑셀 받아올 형태 정하기
results = get_movie_point(1,3)

# pandas 형태로 저장시키기
dataframe = pandas.DataFrame(results, columns=column)
print(dataframe)
dataframe.to_excel("movie.xlsx",
                    sheet_name="네이버영화",
                    header=True,
                    startrow=1)
