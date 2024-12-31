import os
import sys
import pyautogui as pg
from pynput import keyboard  # pynput 라이브러리 추가

# 절대 경로로 모듈 가져오기
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .image_finder_pyautogui import ImageFinder

class TimeController:
    def __init__(self):
        self.image_finder = ImageFinder()  # ImageFinder 인스턴스 생성

    def click_minus(self):
        """타겟 이미지를 찾아 클릭하는 메서드"""
        target_image_path = os.path.join(os.path.dirname(__file__), '../img/baemin_50m.png')  # 타겟 이미지 경로
        abs_path = os.path.abspath(target_image_path)  # 절대 경로로 변환

        # 타겟 이미지 인식
        pos = self.image_finder.find_image(abs_path)
        
        if pos:
            # 특정 부분 클릭을 위한 오프셋 설정
            offset_x = -65  # 클릭할 x 좌표의 오프셋
            offset_y = 0   # 클릭할 y 좌표의 오프셋
            
            # 클릭할 위치 계산
            click_x = pos[0] + offset_x
            click_y = pos[1] + offset_y
            
            # 클릭할 위치를 반환
            return (click_x, click_y)  # 클릭 위치 반환
        else:
            #print("타겟 이미지를 찾을 수 없습니다.")
            return None  # 타겟 이미지가 없을 경우 None 반환
        
    def click_plus(self):
        """타겟 이미지를 찾아 클릭하는 메서드"""
        target_image_path = os.path.join(os.path.dirname(__file__), '../img/baemin_50m.png')  # 타겟 이미지 경로
        abs_path = os.path.abspath(target_image_path)  # 절대 경로로 변환

        # 타겟 이미지 인식
        pos = self.image_finder.find_image(abs_path)
        
        if pos:
            # 특정 부분 클릭을 위한 오프셋 설정
            offset_x = +65  # 클릭할 x 좌표의 오프셋
            offset_y = 0   # 클릭할 y 좌표의 오프셋
            
            # 클릭할 위치 계산
            click_x = pos[0] + offset_x
            click_y = pos[1] + offset_y
            
            # 클릭할 위치를 반환
            return (click_x, click_y)  # 클릭 위치 반환
        else:
            #print("타겟 이미지를 찾을 수 없습니다.")
            return None  # 타겟 이미지가 없을 경우 None 반환