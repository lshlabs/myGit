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

    def find_image(self, image_path):
        """pyautogui와 OpenCV를 사용한 이미지 검색"""
        screenshot = self.take_screenshot()  # 스크린샷을 찍고 파일로 저장
        print(f"스크린샷 크기: {screenshot.shape}")  # 스크린샷 크기 출력
        pos = self.find_by_opencv(screenshot, image_path)  # 파일에서 읽어온 이미지로 템플릿 매칭
        return pos

    def take_screenshot(self):
        """현재 화면의 스크린샷을 찍고 파일로 저장하는 메서드"""
        screenshot_path = './pyQt_test/macro/screenshot/screenshot.png'  # 현재 디렉토리 기준

        # 디렉토리 존재 여부 확인 및 생성
        if not os.path.exists(os.path.dirname(screenshot_path)):
            os.makedirs(os.path.dirname(screenshot_path))  # 디렉토리 생성

        pg.screenshot(screenshot_path)  # 스크린샷을 찍고 파일로 저장

        # 파일 존재 여부 확인
        if not os.path.exists(screenshot_path):
            print(f"스크린샷 파일이 존재하지 않습니다: {screenshot_path}")
            return None

        # 스크린샷이 제대로 찍혔는지 확인
        print(f"스크린샷이 성공적으로 저장되었습니다: {screenshot_path}")

        img_cv = cv.imread(screenshot_path)  # 저장된 파일을 OpenCV로 읽어옴
        return img_cv  # OpenCV 이미지 반환

    def find_by_opencv(self, screenshot, image_path):
        """OpenCV를 사용한 이미지 검색"""
        target = cv.imread(image_path)
        if target is None:
            print(f"타겟 이미지 로드 실패: {image_path}")
            return None

        if screenshot is None:
            print("스크린샷 로드 실패")
            return None

        print(f"타겟 이미지 크기: {target.shape}")  # 타겟 이미지 크기 출력
        res = cv.matchTemplate(screenshot, target, cv.TM_CCOEFF_NORMED)
        
        # 매칭 결과 출력 (디버깅용)
        #print("매칭 결과:", res)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        print(f"최대 매칭 값: {max_val}, 위치: {max_loc}")

        if max_val >= 0.7:  # confidence 값을 0.5로 수정
            h, w = target.shape[:-1]
            click_x = max_loc[0] / self.screen_scale + (w / self.screen_scale) // 2
            click_y = max_loc[1] / self.screen_scale + (h / self.screen_scale) // 2
            return (click_x, click_y)
        return None