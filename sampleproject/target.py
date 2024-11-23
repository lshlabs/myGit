import os
import time
import webbrowser
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg

def is_browser_open():
    try:
        windows = pg.getAllWindows()
        print("현재 열린 창들:")
        for win in windows:
            print(f"- {win.title}")
            if 'Human Benchmark' in win.title or 'humanbenchmark.com' in win.title:
                return True
        return False
    except Exception as e:
        print(f"창 확인 중 오류 발생: {e}")
        return False

# 방법 1: pop의 기본값 설정
os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)

# # 또는 방법 2: 존재 여부 확인 후 제거
# if "QT_QPA_PLATFORM_PLUGIN_PATH" in os.environ:
#     os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

webbrowser.open("https://humanbenchmark.com/tests/aim")
print("브라우저를 여는 중...")
time.sleep(10)
print("대기 완료, 브라우저 상태 확인 중...")

max_attempts = 30
for i in range(max_attempts):
    if is_browser_open():
        print("브라우저가 성공적으로 감지되었습니다.")
        break
    print(f"브라우저 감지 시도 중... ({i+1}/{max_attempts})")
    time.sleep(1)
else:
    print("브라우저를 찾을 수 없습니다. 프로그램을 종료합니다.")
    exit()

print("프로그램 시작")
script_dir = os.path.dirname(os.path.abspath(__file__))
target = cv.imread(os.path.join(script_dir, "target.png"))
render = "pg"
hits = 0

while hits < 31:
    print("새로운 반복 시작...")
    
    if not is_browser_open():
        print("브라우저 창을 찾을 수 없습니다.")
        print("현재 열린 창들:")
        for win in pg.getAllWindows():
            print(f"- {win.title}")
        break

    if render == "pg":
        try:
            print("화면 인식 시도 중...")
            target_path = os.path.join(script_dir, "target.png")
            print(f"타겟 이미지 경로: {target_path}")
            pos = pg.locateOnScreen(target_path, confidence=0.6)
            if pos is None:
                print("타겟을 찾을 수 없습니다. 1초 대기 후 다시 시도합니다.")
                time.sleep(1)
                continue
            
            print(f"인식된 위치: {pos}")
            pg.moveTo(pos[0] + 71, pos[1] + 71)
            pg.click()
            hits += 1
        except TypeError as e:
            print(f"TypeError 발생: {e}")
        except Exception as e:
            print(f"기타 오류 발생: {e}")
    else:
        img = ImageGrab.grab()
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(img_cv, target, cv.TM_CCOEFF_NORMED)
        if (res >= 0.6).any():
            h, w = target.shape[:-1]
            loc = cv.minMaxLoc(res)[-1]
            pg.moveTo(loc[0] + w // 2, loc[1] + h // 2)
            pg.click()
            hits += 1

print(f"프로그램 종료. 총 {hits}번 클릭했습니다.")
