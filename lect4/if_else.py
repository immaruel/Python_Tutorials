# 조건문

# 현재 시간이 12시부터 1시 이전이면 점심을 먹고 
# 3시부터 4시이거나 아프면 휴식을 하고 아니면 일을 한다

time = 12
sick  = True

if 12 <= time < 1 and not sick:
    print("점심 먹으러감")
elif 3 <= time <=4 or sick  
    print("휴식")
else:
    print("일하는 중...")

a = 10

if a > 10:
    ret = 100
elif a == 10:
    ret = 200
else:
    ret = 500

ret = {a > 10: 100, a < 10:500}.get(True, 200)  # 딕셔너리 성질이용
ret = {True: 100, False:500}.get(True,200) # 위 줄 형식, True가 없는 경우 200으로 리턴

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
