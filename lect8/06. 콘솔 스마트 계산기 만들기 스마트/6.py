# 콘솔 스마트 계산기 만들기 스마트 (파이썬기초, 계산기 로직, 리스트, 반복문)
# 사칙연산과 관계 없이 사용자가 입력한 순서대로 계산하는 계산기 만들기


import os
operator = ["+", "-", "*", "/", "="] # 연산자만 따로 모아두는 리스트 만들기

def string_calculator(user_input, show_history=False): # 함수로 만들기
    string_list = [] # 숫자, 공백, 문자를 각각 나누어 리스트 만들기
    lop = 0 # 마지막 연산자의 위치를 기억하는 변수 (last operation position)

    if user_input[-1] not in operator: # 마지막 숫자는 연산자 for문 조건에 해당하지 않으모로 임의로 '='추가
        user_input += "="

    for i, s in enumerate(user_input):
        if s in operator: # 연산자가 s에 있다면 
            if user_input[lop:i].strip() != "":  # 공백을 제거한후(strip()) 마지막 연산자 전까지 공백이 아니라면(=숫자가 있다면)
                string_list.append(user_input[lop:i]) # 리스트에 '숫자' 추가시키기
                string_list.append(s) # 리스트에 '연산자' 추가시키기
                lop = i + 1

    string_list = string_list[:-1] # 마지막 '=' 제거하기
    print(string_list) # 마직막 숫자인 '10'인 빠진 채로 출력됨

    # 계산식 원리 = 연산자 앞뒤의 숫자를 연산자에 따라 계산하고 리스트에서 뺸 후 한 꺼번에 계산 -> 3개씩 묶기
    pos = 0 # 현재 위치를 나타내는 변수 설정
    while True:
        if pos + 1 > len(string_list): # '현재 위치 + 1'이 리스트 길이 보다 크면 정지 
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator: # 현재 위치가 리스트 안에 존재하고 현재 위치가 연산자라면
            temp = string_list[pos-1] + string_list[pos] + string_list[pos +1]
            del string_list[0:3] # 연산자와 함께 계산된 3개 성분을 리스트에서 빼기
            string_list.insert(0, str(eval(temp))) # eval 함수로 단순 계산후 문자열로 캐스팅(str)한후 리스트에 다시 삽입
            pos = 0

            if show_history:
                print(string_list)
        pos += 1
        print(string_list)
    if len(string_list) > 0: 
        result = float(string_list[0]) # 최후로 계산된 값을 실수형으로 변환
    
    return round(result,4) # 소수 4번째 자리까지 나오도록 설정

while True:
    os.system("cls")
    user_input = input("계산식을 입력하세요")   
    if user_input == "/exit":
        break
    result = string_calculator(user_input,show_history=True)
    print("결과 {}".format(result))
    os.system("pause")


