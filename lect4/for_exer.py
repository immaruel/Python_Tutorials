a="abcdefg"
for i in a:
    print(i)

a = ["python","java","c#"]
for language in a:
    print(language)

for i in range(0,100,20):
    print(i)

a = [(1,2),(3,4),(5,6)]
for num in a:
    print(num)

a = [(1,2),(3,4),(5,6)]
for i in a:
    for j in i:
        print(j)

student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for i in student:
    print(i)

student = [{"홍길동":100},{"가가멜":200},{"가제트":300}]
for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value= data[1]
    print("{}. 이름 :{} / 점수:{}".format(s,name,value))

msg = "python programming"
for s, i in enumerate(msg, start=1):
    print(s,i)

result = [num + 5 for num in range(1,6)]
print(result)

result = [num+5 for num in range(1,10) if num % 2 ==0]
print(result) 

gugudan = ["{} x {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1,10)]
print(gugudan)