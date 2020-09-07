# 숫자 야구게임 만들기 (파이썬기초, 랜덤함수, 반복문, 조건문)

import random
import os

numbers = []
number = str(random.randint(0,9)) # 인덱싱('1','2','3')하여 처리하기 위해문자열로 관리

for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

os.system("cls")

print("*"*60)
print("야구 게임을 시작합니다.")

count_strike = 0
count_ball = 0

while count_strike < 3:

    count_strike = 0
    count_ball = 0

    num = str(input("숫자 3자리를 입력하세요 : "))
    if len(num) == 3:
        for i in range(0,3): # 사용자가 입력한 리스트
            for j in range(0,3): # 컴퓨터가 랜덤하게 만든 정답 리스트 (numbers)
                if num[i] == numbers[j] and i == j:  # 자리, 숫자 모두 같은경우 
                    count_strike += 1
                elif num[i] == numbers[j] and i != j: # 자리만 같은 경우
                    count_ball += 1
            if count_strike == 0 and count_ball == 0:
                print("쓰리 아웃!")
            else:
                output = ""
                if count_strike > 0:
                    output += "{} 스트라이크".format(count_strike)
                if count_ball > 0:
                    output += " {} 볼".format(count_ball)
                
                print(output.strip()) # 띄어주기 
print("성공!")