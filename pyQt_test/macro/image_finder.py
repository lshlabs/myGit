import cv2 as cv
import numpy as np
import pyautogui as pg
from PIL import ImageGrab
import os

class ImageFinder:
    def __init__(self):
        # Mac 환경에서의 스케일링 팩터 설정
        if os.name != 'nt':  # Mac 환경인 경우
            self.screen_scale = pg.screenshot().size[0] / pg.size()[0]
        else:
            self.screen_scale = 1

    def find_by_pyautogui(self, image_path):
        """pyautogui를 사용한 이미지 검색"""
        try:
            pos = pg.locateOnScreen(image_path, confidence=0.8)  # confidence 값 0.8로 수정
            if pos:
                # Mac 스케일링 고려한 좌표 계산
                #click_x = pos[0] / self.screen_scale + (71 / self.screen_scale)
                #click_y = pos[1] / self.screen_scale + (71 / self.screen_scale)
                click_x = pos[0] / self.screen_scale + ((pos[2] / 2) / self.screen_scale)
                click_y = pos[1] / self.screen_scale + ((pos[3] / 2) / self.screen_scale)
                return (click_x, click_y)
            return None
        except TypeError:
            return None

    def find_by_opencv(self, image_path):
        """OpenCV를 사용한 이미지 검색"""
        target = cv.imread(image_path)
        img = ImageGrab.grab()
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(img_cv, target, cv.TM_CCOEFF_NORMED)
        
        if (res >= 0.8).any():  # confidence 값 0.8로 수정
            h, w = target.shape[:-1]
            loc = cv.minMaxLoc(res)[-1]
            # Mac 스케일링 고려한 좌표 계산
            click_x = loc[0] / self.screen_scale + (w / self.screen_scale) // 2
            click_y = loc[1] / self.screen_scale + (h / self.screen_scale) // 2
            return (click_x, click_y)
        return None