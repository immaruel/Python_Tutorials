# 영어 단어 맞추기 

import random
import os
words_dict = {
    "사자":"lion",
    "호랑이":"tiger",
    "사과":"apple",
    "비행기":"airplane"
}

os.system("cls")
words = []

for word in words_dict:
    words.append(word)

random.shuffle(words)

chance = 3
for i in range(0,len(words)):
    q = words[i]
    for j in range(0, chance):
        user_input = str(input("{}의 영단어를 입력하세요 : ".format(q)))
        english = words_dict[q]

        if user_input.strip().lower() == english.lower():
            print("정답!")
            break
        else:
            print("오답!")
    if user_input != english:
        print("정답은 {}입니다.".format(english))

print("모든 문제를 다 제출하셨습니다.")