import time
import random
import os

CHO = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] # 초성
JUNG = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"] # 중성
JONG = ["","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] # 종성

def break_korean(string):
    word_list = list(string)
    break_word = []
    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            char_index = ord(k) - ord('가')

            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            char2 = int((char_index / 28) / 21)
            break_word.append(JUNG[char2])

            char3 = int(char_index % 28)
            if char3 > 0:
                break_word.append(JONG[char3])
            else:
                break_word.append(k)
        return break_word
WORD_LIST = [
    "안경환","홍길동","김장원"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip()
    end_time = time.time() - start_time

    src = break_korean(q)
    tar = break_korean(user_input)

    print(src)
    print(tar)

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1
        
        total_len = len(src)
        c = correct / total_len * 100 # 맞는비율 백분율로 표현
        e = (total_len - correct) / total_len * 100 # 틀린 비율 백분율로 표현
        speed = (correct/ end_time) * 60 # 분당 타수
        
        print("속도 : {:0.2f} / 정확도 : {:0.2f} / 오타율 : {:0.2f}".format(speed, c, e))
        os.system("pause")

