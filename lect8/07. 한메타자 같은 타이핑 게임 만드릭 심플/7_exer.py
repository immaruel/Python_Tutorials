import time
import random
import os

WORD_LIST = [
    "안경환","홍길동","김장원"
]

random.shuffle(WORD_LIST)

for q in WORD_LIST: # 리스트에 있는 문자열을 for문을 사용하여 하나씩 담기
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q + '\n')).strip() # 공백이 있으면 지우고 사용자가 문자열을 보고 타이핑 치는 것
    end_time = time.time() - start_time

    if user_input == "/exit":
        break

    correct = 0 # 맞았나 틀렸나를 알기 위한 변수설정
    for i, c in enumerate(user_input):
        if i >= len(q):
            break
        if c == q[i]: # 사용자가 입력한 문자열과 문제가 같으면
            correct += 1 # 맞음의 변수 1 증가시키기
        total_len = len(q)
        c = correct / total_len * 100 # 맞는비율 백분율로 표현
        e = (total_len - correct) / total_len * 100 # 틀린 비율 백분율로 표현
        speed = (correct/ end_time) * 60 # 분당 타수
        
        print("속도 : {:0.2f} / 정확도 : {:0.2f} / 오타율 : {:0.2f}".format(speed, c, e))
        os.system("pause")


