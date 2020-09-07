from pynput.keyboard import Key, Listener, KeyCode

def key_pressed(key):
    print("Pressed {}".format(key))

def key_released(key):
    print("Released {}".format(key))

    if key == Key.esc: #esc 키를 누르면 동작 종료
        return False
with Listener(on_press=key_pressed, on_released=key_released) as listener:
    listener.join()