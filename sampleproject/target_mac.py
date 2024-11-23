import os
import time
import webbrowser
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg

# Mac용 스케일링 팩터 확인
if os.name != 'nt':  # Mac 환경인 경우
    screen_scale = pg.screenshot().size[0] / pg.size()[0]
else:
    screen_scale = 1

os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)

webbrowser.open("https://humanbenchmark.com/tests/aim")
time.sleep(5)

current_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(current_dir, "target_mac.png")

target = cv.imread(target_path)
render = "pg"
hits = 0

while hits < 31:
    if render == "pg":
        try:
            pos = pg.locateOnScreen(target_path, confidence=0.8)
            if pos:
                # Mac에서는 좌표를 스케일링 팩터로 조정
                click_x = pos[0] / screen_scale + (71 / screen_scale)
                click_y = pos[1] / screen_scale + (71 / screen_scale)
                pg.moveTo(click_x, click_y)
                pg.click()
                hits += 1
                print(f"클릭 위치: ({click_x}, {click_y}), 히트 수: {hits}")
        except TypeError:
            pass
    else:
        img = ImageGrab.grab()
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(img_cv, target, cv.TM_CCOEFF_NORMED)
        if (res >= 0.8).any():
            h, w = target.shape[:-1]
            loc = cv.minMaxLoc(res)[-1]
            # Mac에서는 좌표를 스케일링 팩터로 조정
            click_x = loc[0] / screen_scale + (w / screen_scale) // 2
            click_y = loc[1] / screen_scale + (h / screen_scale) // 2
            pg.moveTo(click_x, click_y)
            pg.click()
            hits += 1
            print(f"클릭 위치: ({click_x}, {click_y}), 히트 수: {hits}")