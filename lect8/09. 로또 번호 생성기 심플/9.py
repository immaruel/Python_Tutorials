import random


count =int(input("로또번호를 몇 개 생성할까요? "))

for j in range(count):
    lotto = []

    rand_num = random.randint(1, 46)

    for i in range(6):
        while rand_num in lotto : # 랜덤으로 뽑힐 때 중복성 제거
            rand_num = random.randint(1,46) # 중복될 때 다시 뽑아라
        lotto.append(rand_num)

    lotto.sort() # 낮은 순서부터 출력시키기
    print("{} 로또번호 : {}".format(j, lotto))
