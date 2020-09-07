# ex-1
guest = 1
while guest < 100:
    guest +=1
    print("손님이 {}명입니다".format(guest))
    if guest == 10:
        print("손님이 꽉찼습니다.")
        

#ex-2
num =1 
jjak = 0
hol = 0
while num <= 10:
    if num %2 == 0:
        print("짝수 {}".format(num))
        jjak += num
    else:
        print("홀수 {}".format(num))
        hol += num
    num+=1
print("홀합 {}".format(hol))
print("짝합 {}".format(jjak))

# ex-3
num = 1
hap = 0
while num <= 100:
    hap += num
    num += 1
print("총합 {}".format(hap))