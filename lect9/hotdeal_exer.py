import requests
from bs4 import BeautifulSoup

keyword ="ipad"
def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}".format(keyword)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []
    for r in rows:
        #print(r)
        link = r.select("a.dealTitle.bp-c-link")[0]
        href = link.get("href")
        if href is None:
            continue
        #print(href)
        href = "https://slickdeals.net" + href
        #print(href)

        price = r.select("span.price")[0].text.replace("$","").replace("or","").replace("Less","").strip() # select는 리스트로 출력! -> 태그를 제거하고 ($,Less,or)문자도 제거, 공백도 제거하여 출력
        if price.find("or"or "Less") >= 0 or price == "":
            continue
        # print(price)
        price = float(price)

        hot = len(r.select("span.icon.icon-fire"))
        
        results.append((title, href, price, hot))

    return results

send_lists = []
def main():
    keyword = "ipad"
    max_price = 300.0

    while True:
        results = get_hotdeal(keyword)
        if results is not None:
            for r in results:
                title,href,price,hot = r
                if price < max_price:
                    if title not in send_lists:
                        msg = "{} {} {} {}".format(title, price, hot, href)
                        send_kakao(msg)
                        send_lists.append(title)
            
        time.sleep(60 * 5) # 5분 동안 대기후 목록 받기

main()