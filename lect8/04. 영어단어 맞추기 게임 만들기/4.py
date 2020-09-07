# 영어 단어 맞추기 게임 (파이썬기초, 랜덤함수, 반복문, 조건문, 딕셔너리)

import random
import os
words_dict = {
    "사자":"lion",
    "호랑이":"tiger",
    "사과":"apple",
    "비행기":"airplane"
}

os.system("cls")

words = [] # 딕셔너리는 순서의 개념이 없기에 순서의 개념을 만들기 위해 리스트에 단어 담기
for word in words_dict: 
    words.append(word)

random.shuffle(words) # 리스트에 담긴 영단어 순서 섞기

chance = 3
for i in range(0,len(words)): # 문제 갯수(=4개) 만큼 루프 돌기(반복)
    q = words[i] # 출제할 단어 한개를 리스트에서 끄내기
    for j in range(0, chance):
        user_input = str(input("{}의 영단어를 입력하세요 : ".format(q))) # str 문자열 형태로 casting
        english = words_dict[q] # 출제 리스트의 영단어 가져오기

        if user_input.strip().lower() == english.lower(): # 사용자가 입력한 단어의 공백을 지우고 만약 대문자이면 소문자로 바꾸기
            print("정답!")
            break
        else:
            print("오답!")
    if user_input != english:
        print("정답은 {}입니다." .format(english))

print("모든 문제를 다 제출하셨습니다!")