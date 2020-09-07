import os
import requests
from bs4 import BeautifulSoup

# 1-3-2 파일목록을 구해오는 함수 
def get_dir_list(dir):
    str_list = ""
    if os.path.exists(dir): # dir이 존재하는지 확인
        file_list = os.listdir(dir) # 파일목록을 구해서 변수인 'file_list'에 담기
        file_list.sort() # 파일목록정렬
        for f in file_list:
            full_path = os.path.join(dir,f) # 전체 경로 설정
            if os.path.isdir(full_path):
                f = "[" + f + "]" #폴더일경우 폴더명에 [ ]로 감싸주기
            str_list += f
            str_list += "\n"
        str_list.strip() # 공백제거
        return str_list

#2. 날씨 구해오는 함수
def get_weather(where): #인자 : 궁금한지역
    url = "https://search.naver.com/search.naver?ie=utf8&query={}+날씨".format(where)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    w_box = bs.select("div.today_area > div.main_info")
    #print(w_box)

    if len(w_box) > 0: #오류 방지를 위해 '0'보다 입력한 글자수가 많을 때만 진행
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
