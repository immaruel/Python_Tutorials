# ex-1
def outer_function(msg):
    def inner_function():
        return "난 내부함수인데 {}메세지를 받았어".format(msg)
    return inner_function

c = outer_function("헬로")
print(c())

# ex-2
import time
def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수명 {} 동작시간 {}".format(func.__name__, end_time-start_time))
        return result
    return inner_function

def test():
    start_time  = time.time()
    for i in range(5):
        time.sleep(0.1)
    end_time = time.time() - start_time
    print("함수 동작 시간 : {}".format(end_time))

@time_checker
def test1():
    for i in range(5):
        time.sleep(0.1)

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

test1()
test2()

# ex-3
from functools import wraps

def login_required(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("로그인에 실패하셨습니다")
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    print("안녕")
login()

ex-4 : 태그를 만드는 함수
def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return"<{}>{}</{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator
@add_tag("html")
def test(msg):
    return "반가워" + msg
print(test("홍길동"))