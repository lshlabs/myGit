import json
import os
import threading
import time
from pynput import keyboard  # pynput 라이브러리 추가
from .image_finder_pyautogui import ImageFinder
import pyautogui as pg

class MacroController:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.main_window = main_window  # MainWindow 인스턴스 저장
        self.image_finder_pyautogui = ImageFinder()
        self.running = {}  # 각 메뉴의 실행 상태를 관리하는 딕셔너리
        self.macro_threads = {}  # 각 메뉴의 스레드를 관리하는 딕셔너리
        self.data = json.load(open(self.data_file, 'r', encoding='utf-8'))  # 데이터 파일에서 설정 읽기
        self.register_hotkeys()

    def create_hotkey_combination(self):
        """핫키 조합을 생성하는 메서드"""
        run_dict = {}
        stop_dict = {}
        
        # 각 메뉴에 대한 핫키 조합 생성
        for menu in ['menu2', 'menu3', 'menu6']:
            run_dict[menu] = self._create_hotkey(menu, 'run')
            stop_dict[menu] = self._create_hotkey(menu, 'stop')

        return run_dict, stop_dict  # 각 메뉴에 대한 조합을 반환

    def _create_hotkey(self, menu, action):
        """핫키 조합을 생성하는 헬퍼 메서드"""
        combo_value = self.data[menu]['settings'][f'combo_{action}_value']
        ctrl_state = 'ctrl' if self.data[menu]['settings'][f'check_ctrl{1 if action == "run" else 2}_state'] else None
        alt_state = 'alt' if self.data[menu]['settings'][f'check_alt{1 if action == "run" else 2}_state'] else None
        shift_state = 'shift' if self.data[menu]['settings'][f'check_shift{1 if action == "run" else 2}_state'] else None
        
        return '+'.join(filter(None, [combo_value, ctrl_state, alt_state, shift_state]))

    def register_hotkeys(self):
        """키보드 이벤트 리스너 등록"""
        run_combination, stop_combination = self.create_hotkey_combination()  # 메서드 호출

        # 디버깅 출력
        print(f"menu2 실행 트리거 키 조합: {run_combination['menu2']}")
        print(f"menu2 종료 트리거 키 조합: {stop_combination['menu2']}")
        print(f"menu3 실행 트리거 키 조합: {run_combination['menu3']}")
        print(f"menu3 종료 트리거 키 조합: {stop_combination['menu3']}")
        print(f"menu6 실행 트리거 키 조합: {run_combination['menu6']}")
        print(f"menu6 종료 트리거 키 조합: {stop_combination['menu6']}")

        # 핫키 등록
        hotkey_dict = {
            run_combination['menu2']: lambda: self.start_macro('menu2'),
            stop_combination['menu2']: lambda: self.stop_macro('menu2'),
            run_combination['menu3']: lambda: self.start_macro('menu3'),
            stop_combination['menu3']: lambda: self.stop_macro('menu3'),
            run_combination['menu6']: lambda: self.start_macro('menu6'),
            stop_combination['menu6']: lambda: self.stop_macro('menu6')
        }

        # 빈 문자열 체크 및 핫키 등록
        self.hotkey_listener = keyboard.GlobalHotKeys({
            k: v for k, v in hotkey_dict.items() if k  # 빈 문자열이 아닌 경우만 등록
        })

        self.hotkey_listener.start()
        
        return hotkey_dict

    def _run_macro(self, menu_name):
        """매크로 실행 스레드"""
        menu_data = self.data[menu_name]['other_values']
        image_frames = [k for k in menu_data.keys() if k.startswith('frame_image')]
        
        while self.running.get(menu_name, False):
            for i, frame in enumerate(image_frames):
                if not self.running.get(menu_name, False):
                    break
                    
                image_path = menu_data[frame]
                if image_path:
                    abs_path = os.path.join(os.path.dirname(self.data_file), image_path)
                    filename = os.path.basename(abs_path)
                    
                    # 현재 이미지를 찾을 때까지 계속 시도
                    while self.running.get(menu_name, False):
                        print(f"[{menu_name}] ({filename}) 인식 대기중")
                        pos = self.image_finder_pyautogui.find_image(abs_path)
                        
                        if pos:  # 이미지를 찾았을 때
                            pg.click(pos[0], pos[1])
                            print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: ({filename})\n")
                            break  # 현재 이미지 찾기 루프 종료
                            
                        time.sleep(0.1)
                    
                time.sleep(0.1)

    def start_macro(self, menu_name):
        """매크로 시작"""
        # 데이터 업데이트
        self.data = json.load(open(self.data_file, 'r', encoding='utf-8'))
        
        if not self.running.get(menu_name, False):
            self.running[menu_name] = True
            self.macro_threads[menu_name] = threading.Thread(
                target=self._run_macro, 
                args=(menu_name,)
            )
            print(f"{menu_name} 매크로가 시작되었습니다.")
            self.macro_threads[menu_name].daemon = True
            self.macro_threads[menu_name].start()

    def stop_macro(self, menu_name):
        """매크로 중지"""
        if menu_name in self.running:
            self.running[menu_name] = False
            if menu_name in self.macro_threads:
                self.macro_threads[menu_name].join(timeout=1.0)
                del self.macro_threads[menu_name]
        print(f"{menu_name} 매크로가 중지되었습니다.")
