# 파이썬 예외 처리 try/except, 코딩 진행중 발생한 에러
# 순서 : try -> except - > else -> finally

try: # 실행할 코드
    val = "10.5"
    n = int(val)
except Exception as e:
    print("오류발생 {}".format(e))

test = "100%"
try: 
    number = int(test)
except ValueError:
    print('{}는 숫자가 아닙니다. '.format(test))

try:
    file = open("sample.txt","r")
    n = "10.5"
    v = int(n)
except:
    print("오류발생")
finally:
    file.close()
    print("파이널리 호출")