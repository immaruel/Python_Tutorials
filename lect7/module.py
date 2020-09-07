# 모듈

class FishCakeMaker: # 클래스명
    def __init__(self, **kwargs): # 생성자 , __init__(self) -> 클래스가 최초 생성될 때 호출됨
        self._size = 10       # 기본값
        self._flavor = "팥"   # 기본값
        self._price = 100     # 기본값
        if "size"in kwargs:
            self._size = kwargs.get("size")
        if "flavor"in kwargs:
            self._flavor = kwargs.get("flavor")
        if "price"in kwargs:
            self._price = kwargs.get("price")

    # def __str__(self): # __str__() -> 클래스가 print()에 의해 출력될 때 실행
    #     return("<class FishCakeMaker (size={}, price={},flavoer={}>".format(self._size, self._price, self._flavor))

    # def __del__(self): # 함수 삭제 
    #     print("삭제 되었습니다.")

    def show(self):
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 맛 {}".format(self._flavor))
        print("붕어빵 가격 {}".format(self._price))
        print("*"*50)

# fish1 = FishCakeMaker() 
# fish2 = FishCakeMaker(size=20, price=300)
# fish3 = FishCakeMaker(size=15, price=400,flavor= "초코렛")

# fish1.show()
# fish2.show()
# fish3.show()

class MarketGoods(FishCakeMaker): # MarketGoods는 FishCakeMaker의 클래스를 상속받아 사용
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs) # FishCakeMaker의 상속자 **kwargs를 호출해야함
        self._market_price = self._price + margin
    
    def show(self):
        print(self._flavor, self._market_price)

if __name__ == "__main__": # 이 부분은 수행 x
    fish1 = MarketGoods(size=20, price=500)
    fish1.show()
