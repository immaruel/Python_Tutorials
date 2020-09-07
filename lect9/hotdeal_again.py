import requests
from bs4 import BeautifulSoup
import json
import time

KAKAO_TOKEN = "bIou8z2OQhO-zuB65f8YLC3ETB1ReW-142mvswo9cxcAAAFz0UBmRg"

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
        "button_title": "바로 확인"
    }'
'''

def send_kakao(text):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
            "text": text, # 인자값 text와 동일
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    r = requests.post(url, headers=header, data=data)
    print(r.text)

def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}".format(keyword)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []

    for r in rows:
        # print(i)
        # print(r.select("a.dealTitle.bp-c-link")[0]["href"]) # 원래방식
        
        # href가 없는 경우(None)을 방지하기 위해서 이렇게 작성
        link = r.select("a.dealTitle.bp-c-link")[0]
        href = link.get("href")
        if href is None:
            continue
        # print("https://slickdeals.net" + href)
        href = "https://slickdeals.net" + href
        title = link.text # 타이틀 가져오기
        # print(title, href)

        # select는 리스트 형태
        price = r.select("span.price")[0].text.replace("$","").strip()
        if price.find("or") >=0 or price.find("Less") >= 0 or price == "":
            continue
        price = float(price)
        # print(price)

        hot = len(r.select("span.icon.icon-fire")) # 불꽃이모티콘 유무를 0,1으로 판별
        # print(hot)
        results.append((title, href, price, hot))
    return results

# print(get_hotdeal("ipad"))
send_lists = []
def main():
    keyword = "ipad"
    max_price = 300.0
    while True:
        results = get_hotdeal(keyword)
        if results is not None:
            for r in results:
                title, href, price, hot = r
                if price < max_price:
                    if title not in send_lists:
                        msg = "{} {} {} {}".format(title,price,hot,href)
                        send_kakao()
                        send_lists.append(title)
        time.sleep(60 * 5)

main()

