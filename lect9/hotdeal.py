import requests
from bs4 import BeautifulSoup
import json
import time

KAKAO_TOKEN = "blu1zWteHb-kslsON6FLnKTZSAJKIn_dWvDZ8QopcFAAAAFzza6KAQ"
'''
curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send" \
    -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
    -d 'template_object={
        "object_type": "text",
        "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인" # data는 jason 형태
    }'
'''
def send_kakao(text):
    header = {"Authorization": "Bearer" + KAKAO_TOKEN }
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}

    r = requests.post(url, headers = header, data = data)
    print(r.text)

def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}".format(keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []
    for r in rows:
        # print(r)
        # r.select("a.dealTitle.bp-c-link")[0]["href"] # 원래 방식

        # 혹시 href가 없는 것이 있을 수도 있기에
        link = r.select("a.dealTitle.bp-c-link")[0] # 클래스명이 명확히 있는 경우 중간단계는 생략가능하다
        href = link.get("href") # href가 있으면 가져오고 없으면 None
        if href is None:
            continue
        # print(href) # 폴도멘인 (https:// ~ 이렇게 나오지 않고 일부만 출력)
        href = "https://slickdeals.net" + href
        # print(href)
        title = link.text # 본문내용 가져오기
        # print(title, href) # 본문내용, 주소 출력

        price = r.select("span.price")[0].text.replace("$","").replace("or","").replace("Less","").strip() # select는 리스트로 출력! -> 태그를 제거하고 ($,Less,or)문자도 제거, 공백도 제거하여 출력
        if price.find("or"or "Less") >= 0 or price == "":
            continue
        # print(price)
        price = float(price)

        hot = len(r.select("span.icon.icon-fire")) # 불꽃마크가 있다 없다는 0,1로 판별
        # print(hot)

        results.append((title, href, price, hot)) # 튜플 형태로 담기
    
    return results

#print(get_hotdeal("ipad"))

send_lists = []
def main():
    keyword = "ipad"

    max_price = 300.0
    
    while True:
        results = get_hotdeal(keyword)
        if results is not None:
            for r in results:
                title,href,price, hot = r
                if price < max_price:
                    if title not in send_lists:
                        msg = "{} {} {} {}".format(title, price, hot, href)
                        send_kakao(msg)
                        send_lists.append(title)
            
        time.sleep(60 * 5) # 5분 동안 대기후 목록 받기

main()