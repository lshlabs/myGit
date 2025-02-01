import cv2
import numpy as np
import os
import pyautogui
from PIL import ImageGrab

class ImageFinder:
    def __init__(self):
        # macOS의 Retina 디스플레이 대응
        if os.name != 'nt':  # macOS
            screenshot = ImageGrab.grab()
            self.screen_scale = 2  # Retina 디스플레이의 경우 2배 스케일
        else:  # Windows
            self.screen_scale = 1

    def find_template_matching(self, template_path, screenshot, x1, y1, x2, y2):
        """템플릿 매칭 수행"""
        # 템플릿 이미지 로드
        template = cv2.imread(template_path)
        
        # 지정된 영역 추출
        roi = screenshot[y1:y2, x1:x2]
        
        # 템플릿 매칭 수행
        result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
        
        # 임계값 이상의 매칭 위치 찾기
        threshold = 0.8
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= threshold:  # 매칭이 임계값 이상이면
            # 템플릿 이미지의 크기
            h, w = template.shape[:2]
            
            # ROI 내에서의 중앙 좌표
            center_x = max_loc[0] + w//2
            center_y = max_loc[1] + h//2
            
            # 전체 화면 기준 좌표로 변환
            screen_x = x1 + center_x
            screen_y = y1 + center_y
            
            # Retina 스케일 고려하여 실제 좌표로 변환
            return (screen_x // self.screen_scale, screen_y // self.screen_scale)
        
        return None

    def find_image(self, template_path, x1, y1, x2, y2):
        """이미지 검색 실행"""
        # 전체 화면 스크린샷
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Retina 디스플레이 스케일링 적용
        x1, y1, x2, y2 = x1*self.screen_scale, y1*self.screen_scale, x2*self.screen_scale, y2*self.screen_scale
        
        # 템플릿 매칭 수행
        center_pos = self.find_template_matching(template_path, screenshot, x1, y1, x2, y2)
        
        return center_pos