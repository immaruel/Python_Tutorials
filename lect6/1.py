# 사용자 함수

def 함수명():
    print("함수호출")
    return True

c = 10 #(전역변수)
def add(a,b): # a,b는 매개변수(파라미터)
    global c # 함수내 c 사용 (중요)
    c = a + b # (지역변수)
    return c
b = add(1,10)
print(b,c)

def get_input_user(msg, casting=int):
    ''''사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 리턴한다.

    Args:
        msg (str) : input 시 출력할 문구
        casing (class) : 사용자에게 입력 받은 값의 자료형
    
    Returns:
        user (casting-변수) : 사용자에게 입력받은 값
    
    함수 설명 끝!
    ''''
    while True:
        try:
            user = casting(input(msg)) # user -> 지역변수
            return user
        except:
            continue

user = get_input_user("사용자 이름 입력 : ", str) # 윗 user와 상관없음 , user -> 전역변수 
age = get_input_user("사용자 나이를 입력 : ",int) # 위에서 int를 기본으로 설정했기에 생략가능
print(user, age)

def test1(num):
    num += 10
    print(num)
def test2(lists):
    lists.append("aaaa")
    print(lists)

a = 500 # a 리스트 크기 조정
test1(a) # 리스트 크기 510으로 증가
a = []
a.append("1234")
test2(a)
print(a)

def save_winner(*args): # 튜플형태로 출력
    print(args)

def save_winner2(**kwargs): # 딕션너리형태의 키워드
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])



save_winner("홍길동","가가멜","아즈라엘")
save_winner2(name1= "홍길동", name2="가가멜")

def add(a,b):
    return a + b
def cal(func, a, b): # 함수에 변수담기
    print("결과 {}".format(func(a,b)))
cal(add,1,5)

# 함수 내 함수 설정
def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명: {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function

def add(a,b):
    return a + b

f = outer_function(add)
f(10,20)