import requests
from bs4 import BeautifulSoup

# def get_movie_point(start, end=1):
#     results = []
#     for i in range(start, end+1):
#         url = "https://movie.naver.com/movie/point/af/list.nhn?&page=2"
#         r = requests.get(url)
#         bs = BeautifulSoup(r.text, 'lxml')
#         trs = bs.select("table.list_netizen > tbody > tr")
#         for tr in trs: # 다수의 평점
#             # 번호
#             number = tr.select_one("td.ac.num").text
#             #print(number)
#             # 작성자
#             writer = tr.select_one("td.num > a.author").text
#             #sprint(writer)
        
#         results.append({"number":number, "writer":writer})
#     return results

# print(get_movie_point(1,3))

url = "https://movie.naver.com/movie/point/af/list.nhn?&page=2"
r = requests.get(url)
bs = BeautifulSoup(r.text, 'lxml')
trs = bs.select("table.list_netizen > tbody > tr")
    