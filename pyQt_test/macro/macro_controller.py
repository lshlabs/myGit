import json
import os
import threading
import time
from pynput import keyboard  # pynput 라이브러리 추가
from .image_finder import ImageFinder
import pyautogui as pg

class MacroController:
    def __init__(self, data_file):
        self.data_file = data_file
        self.image_finder = ImageFinder()
        self.running = False
        self.macro_thread = None
        
        # 데이터 파일에서 설정 읽기
        self.load_settings()

        # 키보드 이벤트 리스너 등록
        self.register_hotkeys()

    def load_settings(self):
        """데이터 파일에서 설정을 로드합니다."""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            settings = data.get("settings", {})
            
            # 기본값 설정
            self.combo_run_value = settings.get("combo_run_value", "0")  # 기본값 0
            self.check_ctrl1_state = settings.get("check_ctrl1_state", False)  # 기본값 False
            self.check_alt1_state = settings.get("check_alt1_state", False)  # 기본값 False
            self.check_shift1_state = settings.get("check_shift1_state", False)  # 기본값 False
            self.combo_stop_value = settings.get("combo_stop_value", "1")  # 기본값 1
            self.check_ctrl2_state = settings.get("check_ctrl2_state", False)  # 기본값 False
            self.check_alt2_state = settings.get("check_alt2_state", False)  # 기본값 False
            self.check_shift2_state = settings.get("check_shift2_state", False)  # 기본값 False

    def register_hotkeys(self):
        """키보드 이벤트 리스너 등록"""
        # 핫키 조합 생성
        run_key_combination = self.create_hotkey_combination(self.combo_run_value, self.check_ctrl1_state, self.check_alt1_state, self.check_shift1_state)
        stop_key_combination = self.create_hotkey_combination(self.combo_stop_value, self.check_ctrl2_state, self.check_alt2_state, self.check_shift2_state)

        # 디버깅 출력
        print(f"실행 트리거 키 조합: {run_key_combination}")
        print(f"종료 트리거 키 조합: {stop_key_combination}")

        # 핫키 등록
        self.hotkey_listener = keyboard.GlobalHotKeys({
            run_key_combination: self.start_macro_trigger,  # 실행 트리거
            stop_key_combination: self.stop_macro_trigger   # 종료 트리거
        })
        self.hotkey_listener.start()

    def create_hotkey_combination(self, key_value, check_ctrl, check_alt, check_shift):
        """핫키 조합을 생성하는 메서드"""
        combination = []
        if check_ctrl:
            combination.append('ctrl')
        if check_alt:
            combination.append('alt')
        if check_shift:
            combination.append('shift')
        combination.append(key_value)
        return '+'.join(combination)

    def start_macro_trigger(self):
        """매크로 실행 트리거"""
        print("매크로 실행 트리거 활성화")
        self.start_macro('menu2')  # 예시로 menu2를 사용

    def stop_macro_trigger(self):
        """매크로 종료 트리거"""
        print("매크로 종료 트리거 활성화")
        self.stop_macro()

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
                    
                    found = False  # 이미지가 발견되었는지 여부를 추적하는 변수
                    
                    while not found and self.running:  # 이미지가 발견될 때까지 반복
                        # pyautogui로 먼저 시도
                        pos = self.image_finder.find_by_pyautogui(abs_path)
                        if pos:
                            pg.click(pos[0], pos[1])
                            print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: {image_path}")  # 디버깅용
                            found = True  # 이미지가 발견되었음을 표시
                        else:
                            # opencv로 재시도
                            pos = self.image_finder.find_by_opencv(abs_path)
                            if pos:
                                pg.click(pos[0], pos[1])
                                print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: {image_path}")  # 디버깅용
                                found = True  # 이미지가 발견되었음을 표시
                            else:
                                print(f"이미지 {image_path}를 찾지 못했습니다. 다시 시도합니다.")
                                time.sleep(0.5)  # 잠시 대기 후 재시도

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