import os
import time
import webbrowser
from typing import List
from pathlib import Path

from PIL import ImageGrab
import cv2 as cv
import numpy as np
import pyautogui as pg


os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH", None)  # Only if you get weir errors on startup


class ReflexClicker:
    def __init__(self, max_clicks: int = 5):
        self.images = self._load_images()
        self.current_img = self.images[0]
        self.states = [False, False, False]
        self.click_count = 0
        self.max_clicks = max_clicks

    def _load_images(self) -> List[np.ndarray]:
        current_dir = Path(__file__).parent
        images = []
        for i in range(1, 4):
            img_path = current_dir / f"img0{i}_win.png"
            img = cv.imread(str(img_path))
            if img is None:
                raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {img_path}")
            images.append(img)
        return images

    @staticmethod
    def _get_image() -> np.ndarray:
        return cv.cvtColor(np.array(ImageGrab.grab()), cv.COLOR_RGB2BGR)

    def _set_image_by_state(self) -> None:
        for i, state in enumerate(self.states):
            if not state:
                self.current_img = self.images[i]
                return

    def _update_state(self) -> None:
        for i, state in enumerate(self.states):
            if not state:
                if i == 1:
                    self.click_count += 1
                self.states[i] = True
                break
        
        if all(self.states):
            self.states = [True, False, False]
            time.sleep(2)

    def _get_score(self, screenshot: np.ndarray) -> np.ndarray:
        return cv.matchTemplate(screenshot, self.current_img, cv.TM_CCOEFF_NORMED)

    def run(self) -> None:
        while self.click_count < self.max_clicks:
            self._set_image_by_state()
            screenshot = self._get_image()
            res = self._get_score(screenshot)

            if (res >= 0.8).any():
                h, w = self.current_img.shape[:-1]
                loc = cv.minMaxLoc(res)[-1]
                pg.moveTo(loc[0] + w // 2, loc[1] + h // 2)
                self._update_state()
                pg.click()

def main():
    webbrowser.open("https://humanbenchmark.com/tests/reactiontime")
    time.sleep(5)
    rc = ReflexClicker()
    rc.run()

if __name__ == "__main__":
    main()
