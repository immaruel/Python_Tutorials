from pynput.keyboard import Key, Listener, KeyCode

MY_HOT_KEYS = [
    {"function1":{Key.ctrl, Key.alt_l, KeyCode(char="n")}}
]

current_keys = set()

def function1():
    print("함수 1 호출")

def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]

        if key in KEYS:
            current_keys.add(key)

            if all(k in current_keys for k in KEYS): # 모든 조건이 True여야 True
                    function = eval(FUNCTION)
                    function()
def key_released(key):
    print("Released {}".format(key))

    if key in current_keys:
        current_keys.remove(key)
    if key == Key.esc: #esc 키를 누르면 동작 종료
        return False
with Listener(on_press=key_pressed, on_released=key_released) as listener:
    listener.join()