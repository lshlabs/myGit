import os
import time
import webbrowser

from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg

os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)  # Only if you get weir errors on startup

webbrowser.open("https://humanbenchmark.com/tests/aim")
time.sleep(5)

# 상대 경로 대신 절대 경로 사용
current_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(current_dir, "target.png")

target = cv.imread(target_path)
render = "pg"  # or cv
hits = 0

while hits < 31:
    if render == "pg":
        try:
            pos = pg.locateOnScreen(target_path, confidence=0.6)
            pg.moveTo(pos[0] + 71, pos[1] + 71)
            pg.click()
            hits += 1
        except TypeError:
            pass
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
