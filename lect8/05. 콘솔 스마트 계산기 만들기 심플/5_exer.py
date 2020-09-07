# 콘솔 스마트 계산기 만들기 심플
import os

while True:
    os.system("cls")
    s = input("계산기 입력 :")
    print("결과 = {}".format(eval(s)))
    os.system("pause")