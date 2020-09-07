class CarMixIn:
    def ready(self):
        print("믹스인 레디")
    def start(self):
        print("{}가 {}속도로 달립니다.".format(self.name, self.speed))

class Performance():
    def __init__(self, name, speed):
        self.name = name
        self.seed = speed
        self.ready()

class SuperCar(CarMixIn, Performance): # 두 함수를 상속받음
    def show_info(self):
        print("{}는 {} 속도의 성능입니다.".format(self.name, self.speed))
    def start(self): # CarMixIn에서 지정한 start함수 효력은 없어짐(오버라이딩)
        super().start() # 호력을 다시 살림
        print("스타트")

s = SuperCar("람보르", 300)
s.show_info()
s.start()