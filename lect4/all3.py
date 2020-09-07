# 조건문
# a= 400
# ret = {a>10 : 100, a<10 : 500}.get(True, 200)
# c = 10
# def add(a,b):
#     global c
#     c = a + b
#     return c
# b = add(1,10)
# print(b,c)

# def get_input_user(msg, casting=int):
#     while True:
#         try:
#             user = catsing(input(msg))
#             return user
#         except:
#             continue
# user = get_input_user("사용자 이름 입력 :",str)
# age = get_input_user("사용자 나이 입력 : ", int)
# print(user,age)

def test1(num):
    num += 10
    print(num)
def test2(lists):
    lists.append("aaaa")
    print(lists)
a= 500
test1(a)
a = []
a.append("1234")
test2(a)
print(a)