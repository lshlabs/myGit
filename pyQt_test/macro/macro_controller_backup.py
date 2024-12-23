import json
import os
import threading
import time
from pynput import keyboard  # pynput 라이브러리 추가
from .image_finder import ImageFinder
import pyautogui as pg

class MacroController:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.main_window = main_window  # MainWindow 인스턴스 저장
        self.image_finder = ImageFinder()
        self.running = {}  # 각 메뉴의 실행 상태를 관리하는 딕셔너리
        self.macro_threads = {}  # 각 메뉴의 스레드를 관리하는 딕셔너리
        
        # 데이터 파일에서 설정 읽기
        self.load_settings()
        # 키보드 이벤트 리스너 등록
        self.register_hotkeys()

    def load_settings(self):
        """데이터 파일에서 설정을 로드합니다."""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            current_menu = self.main_window.get_current_menu()  # 현재 선택된 메뉴 가져오기
            # 'other_values'에서 설정 가져오기 (필요한 경우 추가 설정을 로드할 수 있음)
            self.other_values = data[current_menu].get('other_values', {})

    def register_hotkeys(self):
        """키보드 이벤트 리스너 등록"""
        run_combination, stop_combination = self.create_hotkey_combination()  # 메서드 호출

        # 디버깅 출력
        print(f"menu2 실행 트리거 키 조합: {run_combination['menu2']}")
        print(f"menu2 종료 트리거 키 조합: {stop_combination['menu2']}")
        print(f"menu3 실행 트리거 키 조합: {stop_combination['menu3']}")
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

    def create_hotkey_combination(self):
        """핫키 조합을 생성하는 메서드"""
        data = json.load(open(self.data_file, 'r', encoding='utf-8'))
        run_combination = {menu: [] for menu in ['menu2', 'menu3', 'menu6']}
        stop_combination = {menu: [] for menu in ['menu2', 'menu3', 'menu6']}
        
        # 각 메뉴에 대한 핫키 조합 생성
        for menu in run_combination.keys():
            if data[menu]['settings']['combo_run_value']:
                run_combination[menu].append(data[menu]['settings']['combo_run_value'])
            if data[menu]['settings']['check_ctrl1_state']:
                run_combination[menu].append('ctrl')
            if data[menu]['settings']['check_alt1_state']:
                run_combination[menu].append('alt')
            if data[menu]['settings']['check_shift1_state']:
                run_combination[menu].append('shift')
            
            # 조합을 +로 이어서 문자열로 변환
            run_combination[menu] = '+'.join(run_combination[menu])
            
            if data[menu]['settings']['combo_stop_value']:
                stop_combination[menu].append(data[menu]['settings']['combo_stop_value'])
            if data[menu]['settings']['check_ctrl2_state']:
                stop_combination[menu].append('ctrl')
            if data[menu]['settings']['check_alt2_state']:
                stop_combination[menu].append('alt')
            if data[menu]['settings']['check_shift2_state']:
                stop_combination[menu].append('shift')

            stop_combination[menu] = '+'.join(stop_combination[menu])

        return run_combination, stop_combination  # 각 메뉴에 대한 조합을 반환

    def start_macro_trigger(self):
        """매크로 실행 트리거"""
        print("매크로 실행 트리거 활성화")
        self.start_macro(self.main_window.get_current_menu())  # 현재 선택된 메뉴 사용

    def stop_macro_trigger(self):
        """매크로 종료 트리거"""
        print("매크로 종료 트리거 활성화")
        self.stop_macro()

    def _run_macro(self, menu_name):
        """매크로 실행 스레드"""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        menu_data = data[menu_name]['other_values']  # 'other_values'에서 데이터 가져오기
        image_frames = [k for k in menu_data.keys() if k.startswith('frame_image')]
        
        while self.running.get(menu_name, False):
            for frame in image_frames:
                if not self.running.get(menu_name, False):
                    break
                    
                image_path = menu_data[frame]
                if image_path:  # 이미지가 있는 경우만
                    abs_path = os.path.join(os.path.dirname(self.data_file), image_path)
                    
                    found = False  # 이미지가 발견되었는지 여부를 추적하는 변수
                    
                    while not found and self.running.get(menu_name, False):
                        pos = self.image_finder.find_by_pyautogui(abs_path)
                        print("pyautogui 클릭 시도")
                        if pos:
                            pg.click(pos[0], pos[1])
                            print(f"클릭 위치: ({pos[0]}, {pos[1]}), 이미지: {image_path}")  # 디버깅용
                            found = True  # 이미지가 발견되었음을 표시
                        else:
                            # opencv로 재시도
                            pos = self.image_finder.find_by_opencv(abs_path)
                            print("opencv 클릭 시도")
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
        if menu_name not in self.running or not self.running[menu_name]:
            self.running[menu_name] = True
            self.macro_threads[menu_name] = threading.Thread(
                target=self._run_macro, 
                args=(menu_name,)
            )
            self.macro_threads[menu_name].daemon = True
            self.macro_threads[menu_name].start()

    def stop_macro(self, menu_name):
        """특정 메뉴의 매크로 중지"""
        if menu_name in self.running:
            self.running[menu_name] = False
            if menu_name in self.macro_threads:
                self.macro_threads[menu_name].join(timeout=1.0)
                del self.macro_threads[menu_name]
        print(f"{menu_name} 매크로가 중지되었습니다.")