import os
import requests
from bs4 import BeautifulSoup

# 2. 파일 목록 구하는 기능 만들기
def get_dir_list(dir):
    str_list = "" # 문자열 변수
    if os.path.exists(dir): # dir이 존재하는 함수인지 확인
        file_list = os.listdir(dir)
        file_list.sort() # 파일목록 정렬
        for f in file_list:
            full_path = os.path.join(dir, f) # 전체경로 만들기
            if os.path.isdir(full_path):
                f = "[" + f + "]"
            str_list += f
            str_list += "\n"
    str_list.strip()
    return str_list

# 5. 날씨 알려주는 기능 만들기
def get_weather(where):
    weather = ""
    # 5-1. 날씨 정보 크롤링해서 가져오기
    url = "https://search.naver.com/search.naver?&query={}+날씨".format(where)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    w_box = bs.select("div.today_area > div.main_info")
    #print(w_box)

    if len(w_box) > 0: # 오류 방지를 위해 if문 사용
        temperature = bs.select("span.todaytemp")
        cast_text = bs.select("p.cast_txt")
        indicator = bs.select("span.indicator")

        #print(temperature, cast_text, indicator)

        if len(temperature) > 0 and len(cast_text) > 0 and len(indicator) > 0: # 오류방지
            temperature = temperature[0].text.strip() # 공백제거
            txt = cast_text[0].text.strip()
            indicator = indicator[0].text.strip()

            #print(temperature, txt, indicator)

            weather = "{}℃\r\n{}\r\n".format(temperature,indicator,txt)
    return weather


#get_weather("서울")

MONEY_NAME = {
    "유로": "유럽연합 EUR",
    "엔": "일본 JPY (100엔)",
    "위안": "중국 CNY",
    "홍콩달러": "홍콩 HKD",
    "타이완달러": "대만 TWD",
    "파운드": "영국 GBP",
    "달러": "미국USD",
}
# 6. 환율 알려주는 기능 만들기
def get_exchange_info():
    EXCHANGE_LIST = {}
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    trs = bs.select("table.tbl_exchange > tbody > tr")
    for tr in trs:
        tds = tr.select("td")
        name = tds[0].text.strip()
        value = tds[1].text.strip().replace(",","")
        EXCHANGE_LIST[name] = value # name(키), value(값)
    return EXCHANGE_LIST

# 6-1 환전해주는 시스템 함수 만들기
def money_translate(keyword):
    EXCHANGE_LIST = get_exchange_info() #현재 환율 정보구해주기
    keywords = []
    for m in MONEY_NAME.keys():
        if m in keyword:
            keywords.append(keyword[0:keyword.find(m)].strip()) # ex)사용자가 입력한 '달러'라는 글자 찾기
            keywords.append(m)
            break
    #print(keywords)

    if keywords[1] in MONEY_NAME: # '~달러' 라고 입력했으면 "미국USD" 구해오기
        country =MONEY_NAME[keywords[1]]

        if country in EXCHANGE_LIST:
            money = float(EXCHANGE_LIST[country])

            if country == "일본 JPY (100엔)":
                money /= 100
            
            money = format(round(float(money) * float(keywords[0]),3), ",") # 소수 3째 자리까지 구하고 반올림 시킨후 천단위로 콤마찍어주기
            output = "{}원".format(money)
            return output

            
if __name__ == "__main___":
    print(money_translate("150달러"))