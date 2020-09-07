import os
import requests
from bs4 import BeautifulSoup

# 2. 파일 목록 구하는 기능 만들기
def get_dir_list(dir):
    str_list = "" #문자열 변수 설정
    if os.path.exists(dir): # dir이 존재하는 함수인지 확인
        file_list = os.listdir(dir)
        file_list.sort() # 파일 목록 정렬
        for f in file_list:
            full_path = os.path.join(dir, f) # 전체 경로 만들기
            if os.path.isdir(full_path):
                f = "[" + f + "]"
            str_list += f
            str_list += "\n"
    str_list.strip() # 공백제거
    return str_list

# 날씨 알려주는 기능 추가
def get_weather(where):
    weather = "" # 문자열 변수 설정
    url = "https://search.naver.com/search.naver?&query={}+날씨".format(where)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    w_box = bs.select("div.today_area > div.main_info")
    print(w_box)

    if len(w_box) > 0: # 오류 방지를 위해 if문 사용
        temperature = bs.select("span.todaytemp")
        cast_text = bs.select("p.cast_txt")
        indicator = bs.select("span.indicator")

        if len(temperature) > 0 and len(cast_text) > 0 and len(indicator) > 0: # 오류방지
            temperature = temperature[0].text.strip() # 공백제거
            txt = cast_text[0].text.strip()
            indicator = indicator[0].text.strip()

            #print(temperature, txt, indicator)

            weather = "{}℃\r\n{}\r\n".format(temperature,indicator,txt)
    return weather
