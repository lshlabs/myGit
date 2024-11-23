import os
import time
import webbrowser

from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg


os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")  # Only if you get weir errors on startup


class ReflexClicker:
    def __init__(self):
        self.images = (
            cv.imread("img01.png"),
            cv.imread("img02.png"),
            cv.imread("img03.png"),
        )
        self.current_img = self.images[0]
        self.started = 0
        self.states = [False, False, False]
        self.click_count = 0

    @staticmethod
    def _get_image():
        img = ImageGrab.grab()
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        return img_cv

    def _set_image_by_state(self):
        for i, state in enumerate(self.states):
            if not state:
                self.current_img = self.images[i]
                break

    def _update_state(self):
        for i, _ in enumerate(self.states):
            if not self.states[i]:
                if i == 1:
                    self.click_count += 1
                self.states[i] = True
                break
        if all(s for s in self.states):
            self.states = [True, False, False]
            time.sleep(2)

    def _get_score(self, ss):
        return cv.matchTemplate(ss, self.current_img, cv.TM_CCOEFF_NORMED)

    def run(self):
        self._set_image_by_state()
        ss = self._get_image()
        res = self._get_score(ss)

        if (res >= 0.8).any():
            h, w = self.current_img.shape[:-1]
            loc = cv.minMaxLoc(res)[-1]
            pg.moveTo(loc[0] + w // 2, loc[1] + h // 2)
            self._update_state()
            pg.click()

        if self.click_count < 5:
            self.run()


webbrowser.open("https://humanbenchmark.com/tests/reactiontime")
time.sleep(5)
rc = ReflexClicker()
rc.run()
