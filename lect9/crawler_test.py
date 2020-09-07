import requests
from bs4 import BeautifulSoup # 데이터 가공 옵션 1
from requests_html import HTMLSession # 데이터 가공 옵션2


response = requests.get("https://www.naver.com")

print(response.status_code)
print(response.headers)
print(response.text) # 소켓으로 접속해 데이터 받아오기
'''
1. 원하는 웹페이지의 접속하여 html 데이터를 받아온다.
'''
# 옵션1
bs = BeautifulSoup(response.text, "html.parser") # 파이썬 내장함수인 html.parser를 통해 response.text를 분석

'''
2. 받아온 html 데이터를 분석한 가능한 형태로 가공한다.
'''
for img in bs.select("img"):
    print(img) # img 태그를 모아 뽑아라

'''
3. 원하는 데이터를 추출한다. 
'''    
# 옵션2
session = HTMLSession()
response = session.get("https://www.naver.com")
print(response.html.links)