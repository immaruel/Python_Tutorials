사용자가 만드는 함수

c = 10
def add(a,b):
    global c
    c = a + b
    return c 
b = add(1,10)
print(b,c)

def get_input_user(msg, casting=int):
    while True:
        try:
            user = casting(input(msg))
            return user
        except:
            continue
user = get_input_user("사용자 이름 입력 : ", str)
age = get_input_user("사용자 나이 입력 : ")
print(user,age)

def test1(num):
    num += 10
    print(num)
def test2(lists):
    lists.append("aaaaa")
    print(lists)

a = 500
test1(a)
a = []
a.append("1245")
test2(a)
print(a)

def save_winner(*args):
    print(args)
def save_winner2(**kwargs):
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])
save_winner("홍길동","가가멜","아즈라엘")
save_winner2(name1="홍길동",name2="가가멜")

def add(a,b):
    return a + b
def cal(func,a,b):
    print("결과 {}".format(a,b))
cal(add,1,5)

