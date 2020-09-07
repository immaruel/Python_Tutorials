# 데코레이터 : 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념
# 파이썬에서 함수는 일급 객체
# 클로저를 사용하여 함수 내 함수를 정의할 수 있음

#ex-1
def outer_function(msg):
    def inner_function():
        return "난 내부함수인데 {}메세지를 받았어".format(msg)
    return inner_function

c = outer_function("헬로")
print(c())

#ex-2
import time

def time_checker(func):
    def inner_function(*args, **kwarsgs):
        start_time = time.time() 
        result = func(*args, **kwarsgs)
        end_time = time.time()
        print("함수명 {} 동작시간 {}".format(func.__name__, end_time-start_time))
        return result
    return inner_function

def test():
    start_time = time.time() # 시작시간 == 현재시간
    for i in range(5):
        time.sleep(0.1) # 0.5초 동안 슬립이 됨
    end_time = time.time() - start_time
    print("함수 동작 시간 : {}".format(end_time))

test()

@time_checker # 데코레이팅
def test1():
    for i in range(5):
        time.sleep(0.1)

@time_checker # 데코레이팅
def test2():
    for i in range(3):
        time.sleep(0.1)

test1()
test2()

#ex-3
from functools import wraps # functools라는 라이브러리 사용

def login_required(func):
    @wraps(func) # func으로 넘어온 데코레이션을 보존시킴, 항상 붙인다고 생각
    def inner_function(*args, **kwarsgs):
        if not kwarsgs.get("is_login"):
            print("로그인이 되지 않아 수행 불가합니다")
            return "로그인 필요한 페이지 입니다" # 조건 불만족시 나오게 할 메세지
        return func(*args, **kwarsgs) # 조건 만족 시 나오게 할 메세지
    return inner_function

@login_required
def login():
    print("안녕")
login()

#ex-4 : 태그를 만드는 함수
def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}>{}</{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return "반가워" + msg

print(test("홍길동"))


