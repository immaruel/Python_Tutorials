# 반복문 for

# ex-1
a = "abcedfg"
for i in a:
    print(i)

# ex-2
a = ["python","java","c#"]
for i in a:
    print(i)

# ex-3
for i in range(0,100,10): # range(시작값, 끝값+1, 증가값)
    print(i)

# ex-4
a = [(1,2),(3,4),(5,6)]
for i in a:
    print(i)

# ex-5
a = [(1,2),(3,4),(5,6)]
for i in a: # i==(1,2)
    for j in i: 
        print(j)

# ex-6
a = [[[1,2,3,4,5],['a','b','c','d'],[11,12,13]]]
for i in a: # i==[1,2,3,4,5]
    for j in i: 
        for x in j:
            print(x)

# ex-7
student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for i in student:
    print(i)

# ex-8
student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for s, i in enumerate(student, start=1): # s: 카운팅
        data = (list(i.items())[0])
        name = data[0]
        value = data[1]
        print("{} 이름 : {} / 점수 : {}".format(s,name,value))

# ex-9
msg = "python programming"
for s, i in enumerate(msg, start=1):
    print(s,i)

# ex-10
result = []
for num in range(1,6):
    result.append(num + 5)
print(result)

# ex-11
result = [num + 5 for num in range(1,6)] # 윗 줄을 comprehension시키기
print(result)

# ex-12
result = [num + 5 for num in range(1,10) if num % 2 == 0] # 짝수인 경우만 5 더하기
print(result)

# ex-13
for i in range(2,10): # 단 
    for j in range(1,10): #수
        result = i * j
        print (" {} x  {} = {}".format(i,j,result))

gugudan = ["{} x {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
print(gugudan)