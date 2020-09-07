import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

response = requests.get("https://www.naver.com").text

print(response)

bs = BeautifulSoup(response, "html.parser")

for i in bs.select("img"):
    print(i)