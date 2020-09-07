# 숫자 만들기 게임
# import random # 랜덤 라이브러리
# import os # 정돈되게 출력 라이브러리

# chance = 10
# count = 0

# def input_check(msg, casting=int):
#     while True:
#         try:
#             user_input = casting(input("몇 일까요?"))
#             return user_input
#         except:
#             continue

# number= random.randint(1,99)
# os.system("cls")

# print("1부터 99까지의 숫자를 10번 안에 맞춰보세요  ")
# while count < chance:
#     count += 1
#     user_input = input_check("몇 일까요")
#     if number == user_input:
#         break
#     elif number > user_input:
#         print("{} 보다 큰 숫자 입니다.".format(user_input))
#     elif number < user_input:
#         print("{} 보다 작은 숫자 입니다.".format(user_input))
# if user_input == number:
#     print("정답 {}이 맞습니다.".format(number))
# else:
#     print("실패, 정답은 {} 입니다.".format(number))

# # 영단어 맞추기 게임
# import random
# import os
# world_dict ={
#     "사자":"lion",
#     "호랑이":"tiger",
#     "사과":"apple",
#     "비행기":"airplane"
# }
# os.system("cls")

# words = []
# for word in world_dict:
#     words.append(word)

# random.shuffle(words)

# chance = 3
# for i in range(0, len(words)):
#     q = words[i]
#     for j in range(0, chance):
#         user_input = str(input("{}의 영단어를 입력 :".format(q)))
#         english = world_dict[q]

#         if user_input.strip().lower() == english.lower():
#             print("정답")
#             break
#         else:
#             print("오답!")
#     if user_input != english:
#         print("정답은 {} 입니다.".format(english))
# print("모든 문제를 다 제출 했다!")

import random
import os

def input_check(msg, casting=int): # 입력받는 문자를 정수형으로 캐스팅
    while True:
        try:
            user_input = casting(input("몇 일까요?"))
            return user_input
        except:
            continue

    chance = 10
    count = 0

    number = random.shuffle(1,99)
    os.system("cls")

    print("1부터 99까지의 숫자를 10번 안에 맞춰보세여")
    while count < chance:
        count += 1
        user_input == input_check("몇일까요?")
        if number == user_input:
            break
        elif user_input < number:
            print("{} 보다 큰 숫자입니다. ".format(user_input))
        elif user_input > number:
            print("{} 보다 작은 숫자입니다.".format(user_input))
    
    if user_input == number:
        print("정답 {}이 맞습니다. ".format(number))
    else:
        print("실패, 정답은 {}입니다.".format(number))