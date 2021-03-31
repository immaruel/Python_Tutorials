"""
next, iter () 내장함수
iterator : for 반복문에서 'for i in range(100)' 을  통해 0 ~ 99 까지 연속된 숫자를 만들때 사실 이터레이터 하나 생성후 반복하여 숫자를 하나씩 꺼내면서 반복처리
           숫자가 많은 경우 메모리를 많이 사용하게 되어 성능 상 문제가 될수 있음
           이를 해결하기 위해 이터레이터만 생성하고 값이 필요한 시점에 갑을 만드는 방식 사용(지연 평가, lazy evaluation)
           객체가 반복가능한 객체인지 확인하는 방법 : __iter__ 메서드가 있는지 확인
           리스트의 이터레이트를 변수에 저장후 __next__ 메서드를 호출하면 요소를 차례대로 꺼낼수 있음
           __next__로 더 이상 꺼낼 요소가 없는 경우 StopIteration 발생

           __iter__, __next__ 메서드를 구현해서 range(횟수) 와 같이 동작하게 할수있음
"""
class Car:
    def __init__(self,id):
        self.id = id # 차량번호

    def __len__(self):
        return len(self.id)

    def __str__(self):
        return '차량번호' + self.id

    def __call__(self):
        print("__call__함수")
    
    def __iter__(self):
        return(self.id) # 이터레이션인 경우는 자신을 돌려주면됨

def main():
    c = Car("12가 12334")
    for i in c:
        print(i, end = '')


class Coll:
    def __init__(self,values):
        self.values = values # 인자로 전달된 값 저장
        self.call_count = 0 # ___next__ 메서드 호출 횟수
    
    def __next__(self): # 값으 하나씩 반환하고, 값이 없으면 StopIteraion 예외를 발생시킨다
        if len(self.values) <= self.call_count:
            raise StopIteration

        self.call_count += 1
        return self.values[self.call_count - 1]
    
    def __iter__(self):
        self.call_count = 0 # iter() 함수 호출시 next 횟수 초기화
        return self # 객체 자체를 반환 ->몇번이고 호출 가능토록함 

def main2():
    co = Coll([1,2,3,4,5]) # 리스트/ 튜플 / 문자열 등 iterable 객체 전달
    for i in co:
        print(i, end = ' ')
    for i in co:
        print(i, end = ' ')

#main2()

# 이터레이터 만들기
class Counter :
    def __init__(self, stop) :
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자까지 반복
        self.stop = stop    # 반복을 끝낼 숫자

    def __iter__(self) :
        return self         # 현재 인스턴스를 반환

    def __next__(self) :
        if self.current < self.stop :   # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가
            return r                    # 숫자를 반환
        else :
            raise StopIteration         # 예외 발생

def main3():
    for i in Counter(3):
        print(i,end='')

#main3()

# 인덱스로 접근할 수있는 이터레이터 만들기 : _getitem__ 메서드 구현으로 인덱스 접근
class Counter :
    def __init__(self, stop) :
        self.stop = stop

    def __getitem__(self, index) :
        if index < self.stop :
            return index
        else :
            raise IndexError

def main4():
    for i in Counter(3):
        print(i,end='')

main4()