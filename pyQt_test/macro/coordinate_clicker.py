import time
import pyautogui
from pynput.mouse import Controller as MouseController

class CoordinateClicker:
    def __init__(self, data, menu):
        self.mouse = MouseController()
        self.data = data
        self.menu = menu
        self.coordinates = self.data[menu]['coordinates']
        self.is_running = False

    def start(self):
        """좌표 기반 클릭 매크로 시작"""
        self.is_running = True
        
        try:
            # menu에 따라 이미지 개수 설정
            max_images = 6 if self.menu == 'menu6' else 3
            
            # coordinates에서 좌표값이 0이 아닌 것만 필터링
            valid_coordinates = {
                key: (self.coordinates[f'{key}_x'], self.coordinates[f'{key}_y'])
                for key in [f'image{i}' for i in range(1, max_images + 1)]
                if f'{key}_x' in self.coordinates 
                and f'{key}_y' in self.coordinates
                and self.coordinates[f'{key}_x'] != 0 
                and self.coordinates[f'{key}_y'] != 0
            }

            while self.is_running:
                for key, (x, y) in valid_coordinates.items():
                    if not self.is_running:
                        break
                    
                    # 마우스 이동 및 클릭
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    
                    # 딜레이 설정 (필요한 경우 data.json에서 가져올 수 있음)
                    time.sleep(0.5)  # 기본 0.5초 딜레이
                
                # 한 사이클 완료 후 딜레이
                time.sleep(1)  # 기본 1초 딜레이

        except Exception as e:
            print(f"좌표 클릭 매크로 실행 중 오류 발생: {e}")
            self.stop()

    def stop(self):
        """매크로 중지"""
        self.is_running = False

    def is_valid_coordinates(self):
        """유효한 좌표가 있는지 확인"""
        max_images = 6 if self.menu == 'menu6' else 3
        return any(
            self.coordinates[f'image{i}_x'] != 0 and self.coordinates[f'image{i}_y'] != 0
            for i in range(1, max_images + 1)
            if f'image{i}_x' in self.coordinates and f'image{i}_y' in self.coordinates
        ) 