import random

count = int(input("로또번호를 몇 개 생성할까요?"))

for i in range(count):
    lotto = []

    rand_num = random.randint(1,46)

    for j in range(6):
        while rand_num in lotto:
            ran_num = random.randint(1,46)
        lotto.append(rand_num)
    lotto.sort()
    print("{} 로또번호 : {}".format(i, lotto))