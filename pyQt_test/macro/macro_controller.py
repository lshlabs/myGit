# macro/macro_controller.py
import json
import os
import threading
import time
from .image_finder import ImageFinder
import pyautogui as pg

class MacroController:
    def __init__(self, data_file):
        self.data_file = data_file
        self.image_finder = ImageFinder()
        self.running = False
        self.macro_thread = None
    
    def _run_macro(self, menu_name):
        """매크로 실행 스레드"""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        menu_data = data[menu_name]
        image_frames = [k for k in menu_data.keys() if k.startswith('frame_image')]
        
        while self.running:
            for frame in image_frames:
                if not self.running:
                    break
                    
                image_path = menu_data[frame]
                if image_path:  # 이미지가 있는 경우만
                    abs_path = os.path.join(os.path.dirname(self.data_file), image_path)
                    
                    # pyautogui로 먼저 시도
                    pos = self.image_finder.find_by_pyautogui(abs_path)
                    if pos:
                        pg.click(pos[0], pos[1])
                        print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: {image_path}")  # 디버깅용
                    else:
                        # opencv로 재시도
                        pos = self.image_finder.find_by_opencv(abs_path)
                        if pos:
                            pg.click(pos[0], pos[1])
                            print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: {image_path}")  # 디버깅용
            
            time.sleep(0.1)  # CPU 사용량 감소를 위한 짧은 대기
    
    def start_macro(self, menu_name):
        """매크로 시작"""
        if not self.running:
            self.running = True
            self.macro_thread = threading.Thread(
                target=self._run_macro, 
                args=(menu_name,)
            )
            self.macro_thread.daemon = True
            self.macro_thread.start()
    
    def stop_macro(self):
        """매크로 중지"""
        self.running = False
        if self.macro_thread:
            self.macro_thread.join(timeout=1.0)
            self.macro_thread = None