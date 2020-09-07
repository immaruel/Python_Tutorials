# 조건문

# 현재 시간이 12시부터 1시 이전이면 점심을 먹고
# 3시부터 4시이거나 아프면 휴식을 하고 아니면 일을한다.

time = 5
sick = True

if 12 <= time <= 1 and not sick:
    print("점심을 먹으로감")
elif 3<= time <=4  or sick:
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

ret = {a > 10:100, a<10:500}.get(True,200) # 윗문장을 한문장으로 코딩

name = ["김수환","김우식","이정민"]
if "김수환"  in name:
    print("있음")
else:
    print("없음")