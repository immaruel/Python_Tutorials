# lect4
조건문 if-else

# ex-1
time = 12
sick = True

if 12 <= time <= 1 and not sick:
    print("점심먹기")
elif 3 <= time <= 4 or sick:
    print("휴식")
else:
    print("일하자 ")

# ex-2
a = 10

if a > 10:
    ret = 100
elif a ==10:
    ret = 200
else:
    ret = 500
ret = {a > 10:100, a < 10:500}.get(True,200)
ret = {True: 100,Fale:500}.get(True,200)

# ex-3
name = "abcdef"
if "ㅋ" in name:
    print("있음")
else:
    print("없음")

# ex -4
name = ["안","경","환"]
if "장" in name:
    print("있음")
else:
    print("없음")


조건문 while

# ex -1 
guest = 1
while guest < 10:
    guest += 1
    print("손님이 {}명입니다.".format(guest))
    if guest == 10:
        print("손님이 꽉찼다.")

# ex -2 
num = 1
jjak = 0
hol = 0
while num <= 10:
    if num % 2 == 0:
        print("짝수 {}".format(num))
        jjak += num
    else:
        print("홀수 {}".format(num))
        hol += num
    num += 1
print("홀수의 합 {} ".format(hol))
print("짝수의 합 {} ".format(jjak))

조건문 for
# ex-1
a = "abcdef"
for i in a:
    print(i)

# ex-2 
a = ["python","c#","jsp"]
for i in a:
    print(i)

# ex-3
for i in range(0,101,20):
    print(i)

# ex-4
a = [(1,2),(3,4),(5,6)]
for i in a:
    print(i)

# ex - 5
student = [{"홍길동":100}, {"가가멜":200}, {"가제트":300}]
for i in student:
    print(i)

# ex -6
student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for s, i in enumerate(student, start=1): # s: 카운팅
        data = (list(i.items())[0])
        name = data[0]
        value = data[1]
        print("{} 이름 : {} / 점수 : {}".format(s,name,value))

# ex -7
msg = "python programming"
for s , i in enumerate(msg, start=1):
    print(s,i)

# ex -8
result = []
for num in range(1,6):
    result.append(num + 5)
print(result)

for i in range(2,10):
    for j in range(1,10):
        result = i * j
        print("{} X {} = {}".format(i,j,result))


# lect5
사용자 입력받기
num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))
print(num1 + num2)

langs = ["한국어","중국어","일본어"]
for s, langs in enumerate(langs, start=1):
    print("{}. {} ".format(s,langs))

while True:
    sel = input("언어를 선택하세요 : ")

    if not sel.isnumeric():
        continue
    sel = int(sel)
    if 0 < sel < 3:
        break

print("사용자가 선택한 언어는 {}입니다. ".format(langs[sel-1]))

# 입력한 숫자가 소수인지 판단
while True:
    num = input("2이상의 숫자를 입력 : ")
    if not num.isnumeric(): # 숫자가 아니라면 다시 조건으로 돌아가기
        continue
    num = int(num) 
    if num < 2:
        continue
    break

isprime = True 
for  n in range(2,num):
    if num % 2 == 0:
        isprime = False
        break
if isprime:
    print("소수입니다.")
else:
    print("소수 아님")

파이썬 파일을 읽고 쓰기
file = open("sample.txt", mode="w",encoding="utf-8")
file.write("안녕파이썬")
file.close()

with open("sample.txt", mode="r", encoding="utf-8")as s, open("sample2.txt",mode="w",encoding=utf-8) as t:
    t.write(s.read().replace("파이썬","ㅇㅇ"))

파이썬 예외 처리 : try, except -> 코딩 진행중 발생한 에러처리
# ex -1
try:
    val = "10.5"
    n = int(val)
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류발생 {}".format(e))

# ex -2
text = "100.2"
try:
    number = int(text)
except ValueError:
    print("{}는 숫자가 아님".format(text))

# ex -3
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else:
        print("{} index를 가져올수 없다".format(index))

사용자가 만든 함수

# ex-1
c = 10  # 전역 변수
def add(a,b):
    global c
    c = a + b
    return c

b = add(1,13)
print(c)


# ex -2
def get_input_user(msg, casting=int):
    while True:
        try:
            user = casting(input(msg))
        except:
            continue

user = get_input_user("사용자 이름 입력 : ",str)
age = get_input_user("사용자 이름 입력 : ",int)
print(user, age)

# ex-3
def test1(num):
    num += 10
    print(num)
def test2(lists):
    lists.append("aaaa")
    print(lists)

a = 500
test1(a)
a = []
a.append("1234")
test2(a)
print(a)

# ex-4
def save_winner(*args):
    print(args)
def save_winner2(**kwargs):
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])
save_winner("홍길동","가가멜","아즈라엘")
save_winner2(name1 = "홍길동", name2="가가멜")

