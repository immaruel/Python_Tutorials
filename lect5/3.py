# 파이썬 예외 처리 try / except,  코딩 진행중 발생한 에러   
# 순서 : try -> except -> else -> finally
#ex-1
try: # 실행할 코드
    val = "10.5"
    n = int(val)
    idx = []
    idx[0] = 100
except Exception as e: # 예외가 발생했을 때 실행되는코드 
    print("오류발생 {}".format(e))

#ex-2
text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아닙니다.'.format(text)


#ex-3
# try-except 문   
def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올수 없습니다.'.format(index))

# if-else 문 : 경우에 따라서 if문을 사용하는게 좋을 때도 있다.
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올수 없습니다.'.format(index))

#ex-4
try:
    file = open("sample.txt", "r")
    n = "10.5"
    v = int(n)
except:
    print("오류발생")
finally: # try-except절에서 예외의 발생여부와 상관없이 항상 실행됨
    file.close()
    print("파이널리 호출")