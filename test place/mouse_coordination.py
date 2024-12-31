from pynput import mouse, keyboard

# 종료 키 설정 (예: ESC 키)
exit_key = keyboard.Key.esc

def on_click(x, y, button, pressed):
    if pressed:
        print(f'클릭한 좌표: ({x}, {y})')

def on_press(key):
    if key == exit_key:
        print("프로그램을 종료합니다.")
        return False  # 리스너 종료

# 마우스 리스너 시작
with mouse.Listener(on_click=on_click) as mouse_listener, \
     keyboard.Listener(on_press=on_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()