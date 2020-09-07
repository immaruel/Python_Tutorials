time = 12
sick = True

if 12 <= time <= 1 and not sick:
    print("점심 먹으러감")
elif 3 <= time <= 4 or sick:
    print("휴식")
else:
    print("일하는중")

a = 10
if a > 10:
    ret = 100
elif a == 10:
    ret = 200
else:
    ret = 500
a=10
ret = {a >10:100, a<10:500}.get(True,200)
print(ret)

name = "abcdef"
if "a"in name:
    print("있음")
else:
    print("없음")

name = ["홍길동","가제트","나루토"]
if "나루토" in name:
    print("있음")
else:
    print("없음")

guest = 1
while guest < 10:
    print("손님이 {}명입니다.".format(guest))
    guest+=1
    if guest == 10:
        print("손님이 꽉찼습니다.")

num = 1
jjak = 0
hol = 0
while num <= 10:
    if num % 2 == 0:
        print("짝수 {}".format(num))
        jjak += num
    else:
        print('홀수 {}'.format(num))
        hol += num
    num +=1
print("홀수의 합 {}".format(hol))
print("짝수의 합 {}".format(jjak))

a = "abcdefg"
for i in a:
    print(i)

a = ["파이썬","자바","C"]
for i in a:
    print(i)

for i in range(0,101,20):
    print(i)

student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for i in student:
    print(i)

student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{}. 이름 : {} / 점수 : {}".format(s, name,value))

msg = "python programming"
for s, i in enumerate(msg, start=1):
    print(s,i)

result = [num + 5 for num in range(1,6)]
print(result)

result = [num+4 for num in range(1,11) if num % 2 == 0]
print(result)

gugudan = ["{} x {} = {}".format(i,j,i*j) for i in range(2,11) for j in range(1,10)]
print(gugudan)