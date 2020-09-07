import time
import random
import os

WORD_LIST = [
    "한국 외교관이 뉴질랜드 근무 당시 현지 남자 직원을 성추행했다는 의혹을 두고 문재인 대통령이 뉴질랜드 총리에게 사실관계 확인 후 처리하겠다는 입장을 밝힌 것으로 알려졌다."
    "청와대 핵심관계자는 29일 기자들과 만나 전날 한·뉴질랜드 정상통화를 언급하며 전했다."
    "강민석 청와대 대변인은 전날 문 대통령과 저신다 아던 뉴질랜드 총리의 정상통화 관련 서면브리핑"
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


