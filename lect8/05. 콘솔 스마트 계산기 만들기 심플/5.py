# 콘솔 스마트 계산기 만들기 심플 (파이썬기초, 계산기 로직, 리스트, 반복문, eval 함수)
import os

while True:
    os.system("cls")
    s = input("계산식 입력 : ")
    print("결과 : {}".format(eval(s))) # eval함수-> string을 계산식으로 바꿔 주는 함수
    os.system("pause") # 실행 후 잠깐 정지 
