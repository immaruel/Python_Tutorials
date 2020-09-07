# 사용자 입력받기

# num1 = int(input("숫자1 : "))
# num2 = int(input("숫자2 : "))
# print(num1 + num2)

# langs = ["한국어","중국어","일본어"]
# for s, langs in enumerate(langs, start=1):
#     print("{}. {}".format(s,langs))

# while True:
#     sel = input("언어를 선택하세요 : ")

#     if not sel.isnumeric():
#         continue
#     sel = int(sel)
#     if 0 < sel < 3:
#         break

# print("사용자가 선택한 언어는 {}입니다. ".format(langs[sel-1]))


# 입력한 숫자가 소수 인지 판단

# while True:
#     num = input("2이상의 숫자를 입력하세여 : ")
#     if not num.isnumeric():
#         continue
#     num = int(num)
#     if num < 2:
#         continue
#     break

# while True:
#     isprime= True
#     for n in range(2,num):
#         if num % n == 0:
#             isprime = False
#             break
#     if isprime:
#         print("소수 입니다.")
#     else:
#         print("소수가 아니다.")
#     break