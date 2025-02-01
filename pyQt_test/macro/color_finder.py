import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import os

class ColorFinder:
    def __init__(self):
        # macOS의 Retina 디스플레이 대응
        if os.name != 'nt':  # macOS
            screenshot = ImageGrab.grab()
            self.screen_scale = 2  # Retina 디스플레이의 경우 2배 스케일
        else:  # Windows
            self.screen_scale = 1

    def detect_app_by_icon(self, image):
        """색상 기반 앱 감지"""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # 마스크 생성 및 픽셀 계산
        red_mask = cv2.bitwise_or(
            cv2.inRange(hsv, np.array([0, 150, 100]), np.array([10, 255, 255])),
            cv2.inRange(hsv, np.array([170, 150, 100]), np.array([180, 255, 255]))
        )
        mint_mask = cv2.inRange(hsv, np.array([85, 100, 100]), np.array([95, 255, 255]))
        
        red_pixels = cv2.countNonZero(red_mask)
        mint_pixels = cv2.countNonZero(mint_mask)
        
        # 결과 판단 (임계값 미세 조정)
        if red_pixels > 1000:
            return "요기요"
        elif mint_pixels > 2000:
            return "배민"
        return "알 수 없음"

    def find_color(self, x1, y1, x2, y2):
        """색상 검색 실행"""
        # 전체 화면 스크린샷
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Retina 디스플레이 스케일링 적용
        x1, y1, x2, y2 = x1*self.screen_scale, y1*self.screen_scale, x2*self.screen_scale, y2*self.screen_scale
        
        # 지정된 영역 추출
        roi = screenshot[y1:y2, x1:x2]
        
        # 앱 감지
        result = self.detect_app_by_icon(roi)
        
        return result
