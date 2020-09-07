'''
한글ord = ((초성 * 21) + 중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) /21
중성 = ((x -44032) / 28) % 21
종성 = (x- 44032) % 28

'''
import time
import random
import os

CHO = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] # 초성
JUNG = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"] # 중성
JONG = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] # 종성

def break_korean(string): # 입력받은 문자를 초,중,종성으로 나눠 리스트에 담는 함수
    word_list = list(string)
    break_word = [] # 분리된 문자를 담는 리스트
    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"): # 주어진 조건내에 있으면 조립된 한글임
        # 유니코드 상 몇 번째 글자인지 인덱스를 구한다.
            char_index = ord(k) - ord('가') # '가'는 유니코드의 첫번째 글자로 44032와 같다 -> (x-44032) = 유니코드인덱스
        
            # 초성, 중성, 종성 분리시키기
            # 초성 = (유니코드 인덱스 / 28) /21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1]) #  리스트에 추가


            #중성 = (유니코드인덱스 / 28) % 21
            char2 = int((char_index / 28) / 21)
            break_word.append(JUNG[char2]) #  리스트에 추가

            #종성 = (유니코드인덱스 % 28)
            char3 = int(char_index % 28)     

            if char3 > 0: # 종성에 받침이 없는 경우 대비
                break_word.append(JONG[char3]) #  리스트에 추가
            
            else: # 만약 한글이 아닌 문자는 따로 추가시키기
                break_word.append(k) 
    return break_word

WORD_LIST = [
    "안경환","홍길동","김장원"
]

random.shuffle(WORD_LIST)


for q in WORD_LIST: # 리스트에 있는 문자열을 for문을 사용하여 하나씩 담기
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip() # 공백이 있으면 지우고 사용자가 문자열을 보고 타이핑 치는 것
    end_time = time.time() - start_time

    src = break_korean(q) # 문제 쪼개기
    tar = break_korean(user_input) # 사용자가 입력한 문자 쪼개기

    if user_input == "/exit":
        break

    correct = 0 # 맞았나 틀렸나를 알기 위한 변수설정
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]: # 사용자가 입력한 문자열과 문제가 같으면
            correct += 1 # 맞음의 변수 1 증가시키기

        total_len = len(src)
        c = correct / total_len * 100 # 맞는비율 백분율로 표현
        e = (total_len - correct) / total_len * 100 # 틀린 비율 백분율로 표현
        speed = (correct/ end_time) * 60 # 분당 타수
        
        print("속도 : {:0.2f} / 정확도 : {:0.2f} / 오타율 : {:0.2f}".format(speed, c, e))
        os.system("pause")



  
  