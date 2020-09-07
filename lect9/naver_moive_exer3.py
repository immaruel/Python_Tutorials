import requests
from bs4 import BeautifulSoup
import pandas

def get_movie_point(start, end=1):
    result = []
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
            
            # title
            tr_data = tr.select_one("td.title")
            ## title 중 a 태그 가져오기
            title = tr_data.select_one("a").text
            ## title 중 a 태그 중 div 중 em 태그 의 점수 추출
            point = tr_data.select_one("div.list_netizen_score > em").text

             # td class="title" 태그에서 a, div, br 태그 제거
            # extract() 함수는 태그와 태그의 내용까지 모두 제거합니다.
            [x.extract() for x in tr_data.select("a")]
            [x.extract() for x in tr_data.select("div")]
            [x.extract() for x in tr_data.select("br")]

            # 위에서 태그를 모두 제거한 tr_data에서 내용만 추출
            content = tr_data.text.strip()
            results.append({
                "number": number,
                "movie": title,
                "point": point,
                "writer": writer,
                "contents": content,
            })
    return results

print(get_movie_point(1,1))

        