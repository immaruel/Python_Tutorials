import time
import threading # 함수 동시 일 시키기

def 주문받기():
    for i in range(5):
        print("주문받기 {}".format(i))
        time.sleep(1)

def 우편발송():
    for i in range(5):
        print("우편발송 {}".format(i))
        time.sleep(5)

th1 = threading.Thread(target=주문받기)
th2 = threading.Thread(target=우편발송)

th1.daemon = True # 메인 쓰레드가 중지되어도 중지 되지 않게함
th2.daemon = True

th1.start()
th2.start()