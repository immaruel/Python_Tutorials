"""
1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
3. 정해진 자릿수 만큼 연속 숫자를 포함하는 번호를 생성하는 기능
"""

import numpy # numpy : 다차원 배열 계산에 사용되는 라이브러리

def make_lotto_number(**kwargs): # kwargs:키워드 형태로 입력받음
    rand_number = numpy.random.choice(range(1,46),6, replace=False) # 1 부터 46까지 숫자 중 6개를 중복되지 않게 뽑아라
    rand_number.sort() # 뽑은 6개 정렬
    
    lotto = [] # 최종 로또 번호가 완성될 변수

    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include) # append 와 다르게 extend는 리스트가 통쨰로 들어오더라도 원소하나하나씩 리스트에 추가시킴

        cnt_make = 6 - len(lotto) # 만약 1,2가 들어가 있다면 4자리만 더 뽑으면됨 

        for _ in range(cnt_make): # 만약 len(lotto) = 2라면 4번 반복문 실행
            for j in rand_number: # rand_number : 위에서 중복없이 만든 6개
                if lotto.count(j) == 0: # 중복없이 만든 6개와 [1,2]가 겹치는 게 없으면 '0'
                    lotto.append(j)
                    break
    else: # [1,2] 와 같은 include 옵션이 없는경우
        lotto.extend(rand_number) # 애초에 중복없이 뽑은 6자리 
    '''
    여기 줄 까지  1. 특정 숫자를 포함해서 로또 번호를 생성해주는 기능
    '''

    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) -set(exclude)) # 집합은 중복을 허용 하지 않으므로 집합사용, 위에서 결정 6자리 수 리스트에서 exclude로 결정 6자리를 뺀 리스트 생성

        while len(lotto) != 6: # 차집합으로 빠진만큼 추가로 뽑기
             for _ in range(6 - len(lotto)):
                 rand_number = numpy.random.choice(range(1,46),6, replace=False)
                 rand_number.sort()

                 for j in rand_number:
                     if lotto.count(j) == 0 and j not in exclude:
                         lotto.append(j)
                         break

    '''
    여기 줄 까지 2. 특정 숫자를 제외해서 로또 번호를 생성해주는 기능
    '''

    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto,1) # lotto리스트에 있는 원소 한개를 임의대로 사용
        
        seq_num = []# 연속된 번호를 저장할 리스트 생성

        for i in range(start_number[0],start_number[0]+ continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = [] # 기존 로또번호를 초기화한후 새로 만들어 리스트에 담음
        lotto.extend(seq_num)

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1,46),6, replace=False)
                rand_number.sort()

                for j in rand_number: 
                    if lotto.count(j) == 0 and j not in seq_num:
                        lotto.append(j)
                        break

                lotto = list(set(lotto))
    lotto.sort()
    return lotto

    '''
    여기 줄 까지 3. 정해진 자릿수 만큼 연속 숫자를 포함하는 번호를 생성하는 기능
    '''
    
print(make_lotto_number(include=[1,2])) # 1,2가 포함된 로또 번호를 뽑겠다.
print(make_lotto_number(exclude=[1,2])) # 1,2가 포함되지 로또 번호를 뽑겠다.
print(make_lotto_number(continuty =6)) # 세자리가 연속된 로또번호를 뽑겠다