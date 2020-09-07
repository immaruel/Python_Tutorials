import requests
from bs4 import BeautifulSoup
import re # 정규식 내부 라이브러리
import json
import random
import os

def get_news():
    url = "https://www.usatoday.com"
    # 1. 뉴스 탑텐기사 10개 가져오기
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'lxml')
    lists = bs.select("div.gnt_m_th > a.gnt_m_th_a")
    for li in lists:
        href = url + li["href"]
        
        # 선택된 탭 페이지로 이동
        r = requests.get(href)
        bs = BeautifulSoup(r.text, 'lxml')
        texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")
        contents = [p.text for p in texts] # 태그 없이 기사 내용만 출력(리스트 형태)
        contents = " ".join(contents) # 리스트를 벗기고 하나의 문자열로 출력
        #print(contents)
        return contents.lower() # 소문자로 바꾸기, for문이 반복되지 않고 한번만 돌고 종료
    return None
#print(get_news()) # 한개의 뉴스 기사만 출력

# 4. 한글사전에서 한글번역본 가져오기
def naver_translate(word): 
    try:
        url = "https://ac.dict.naver.com/enkodict/ac?st=11001&r_lt=11001&q={}".format(word) # 주소가 json형태
        r = requests.get(url)
        j = json.loads(r.text) # 변수j에 담기
        return (j["items"][0][0][1][0]) # 글자만 받아오기 해당하는 것은 직접 찍어봐야함
    except: # 오류가 발생한 경우
        return None

# 2. 4~15자의 수를 가지는 영단어만 출력시키기 -> 정규식 사용
def make_quize(news):
    match_pattern = re.findall(r'\b[a-z]{4,15}\b',news)

    # 3. 출력된 단어가 몇번 나오는지 카운팅
    frequency = {} # 딕셔너리 형태 -> 영단어 : key, 카운팅 : value
    quize_list = [] # 한글(번역단어)를 담을 리스트 설정

    for word in match_pattern:    
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    for word, count in frequency.items():
        #print(word,count)
        if count > 1: # 문서에 해당 단어가 존재한다면
            kor = naver_translate(word)

            if kor is not None:
                quize_list.append({kor:word}) # 딕셔너리 형태 -> 한글:key, 영단어:value
    return quize_list

def quize():
    quize_list = make_quize(get_news())
    random.shuffle(quize_list) # 영단어 섞기

    chance = 5
    count = 0 
    for q in quize_list: # q에 영단어와 한글이 들어가 있음
        os.system("cls") # 새문제가 나올떄마다 화면 백지화
        count += 1 # 남은 문제를 확인하기 위해 카운팅 사용
        kor = list(q.keys())[0] # 딕셔너리 형태로 저장되어 있으므로 강제로 리스트로 형변환
        english = q.get(kor)

        print("*"*90)
        print("문제 : {}".format(kor))
        print("*"*90)

        for j in range(chance):
            user_input = str(input("위의 뜻이 의미하는 단어를 입력하세요 : ")).strip().lower() # 입력받은 영단어를 소문자, 공백이 있다면 제거

            if user_input == english:
                print("정답입니다! {} 문제남음".format(len(quize_list)-count))
                os.system("pause")
                break
            else:
                n = chance - (j + 1) # 5 - 기회(0부터 시작하니까)
                if j == 0:
                    print("{}가 아닙니다. {}번의 기회가 남았습니다".format(user_input, n))
                elif j == 1: # 두번쨰 시도
                    print("{}가 아닙니다. {}번의 기회가 남았습니다. 힌트 : {}로 시작!".format(user_input, n, english[0])) # 힌트 : 영단어의 첫글자만 알려줌
                elif j == 2: # 두번쨰 시도
                    hint =" - " * (len(english) -2) # 남은 문자를 밑줄로 힌트주기
                    print("{}가 아닙니다. {}번의 기회가 남았습니다. 힌트 : {} {} {}로 시작!".format(user_input, n, english[0], english[1], hint)) # 힌트 : 영단어의 첫글자만 알려줌
                elif j == 3: # 두번쨰 시도
                    hint =" - " * (len(english) -3) # 남은 문자를 밑줄로 힌트주기
                    print("{}가 아닙니다. {}번의 기회가 남았습니다. 힌트 : {} {} {} {} 로 시작!".format(user_input, n, english[0], english[1],english[2], hint)) # 힌트 : 영단어의 첫글자만 알려줌
                else:
                    print("틀렸습니다! 정답은 {}입니다".format(english))
                    os.system("pause")
        print("더이상 문제가 없습니다!")
quize()
# quize = make_quize(get_news())
# naver_translate("man") # 불필요한 리스트 확인을 위해 찍어보자!