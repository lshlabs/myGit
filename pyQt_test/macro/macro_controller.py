import json
import os
import threading
import time
from pynput import keyboard  # pynput 라이브러리 추가
from .image_finder import ImageFinder
import pyautogui as pg
from .hotkey_manager import HotkeyManager

class MacroController:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.main_window = main_window
        self.image_finder_pyautogui = ImageFinder()
        self.running = {}  # 각 메뉴의 실행 상태
        self.macro_threads = {}  # 각 메뉴의 스레드
        self.data = json.load(open(self.data_file, 'r', encoding='utf-8'))
        self.completed_frames = {}  # 각 메뉴의 완료된 프레임 수
        self.frame1_detected = {}  # frame_image1 감지 상태
        self.frame1_order = []  # frame_image1이 감지된 메뉴 순서
        self.current_cycle_menu = None  # 현재 frame2,3 실행 중인 메뉴
        
        # 핫키 매니저 초기화 및 등록
        self.hotkey_manager = HotkeyManager(self)
        self.hotkey_manager.register_hotkeys()

    def _run_macro(self, menu_name):
        """매크로 실행 스레드"""
        menu_data = self.data[menu_name]['other_values']
        time_adjusted = False  # 시간 조정 완료 플래그
        
        while self.running.get(menu_name, False):
            # frame_image1 감지
            if not self.frame1_detected.get(menu_name, False):
                # 매 사이클마다 시간 조정 실행
                if not time_adjusted:
                    # entry1이 50이면 시간 조정 건너뛰기
                    if menu_data['entry1'] == 50:
                        print(f"[{menu_name}] 배달시간이 조정이 필요하지 않습니다.\n")
                        time_adjusted = True
                    else:
                        self.adjust_time(menu_name, menu_data)
                        time_adjusted = True

                if self._detect_frame1(menu_name, menu_data):
                    self.frame1_detected[menu_name] = True
                    self.completed_frames[menu_name] = 1
                    if menu_name not in self.frame1_order:
                        self.frame1_order.append(menu_name)
                    continue

            # frame1_order가 비어있으면 continue
            if not self.frame1_order:
                time.sleep(0.1)
                continue

            # frame_image2, frame_image3 처리
            # 현재 메뉴가 frame1_order의 첫 번째가 아니면 대기
            if menu_name != self.frame1_order[0]:
                time.sleep(0.1)
                continue

            # frame_image2, frame_image3 순차 실행
            for frame in ['frame_image2', 'frame_image3']:
                if not self.running.get(menu_name, False):
                    break
                self._process_image(menu_name, frame, menu_data)

            # 한 사이클 완료 후 상태 초기화
            self.frame1_detected[menu_name] = False
            self.completed_frames[menu_name] = 0
            time_adjusted = False  # 시간 조정 완료 플래그도 초기화
            # frame1_order에서 현재 메뉴 제거 (리스트가 비어있지 않은 경우에만)
            if self.frame1_order and self.frame1_order[0] == menu_name:
                self.frame1_order.pop(0)

    def _detect_frame1(self, menu_name, menu_data):
        """frame_image1 감지 및 처리"""
        image_path = menu_data.get('frame_image1')
        if not image_path:
            return False

        abs_path = os.path.join(os.path.dirname(self.data_file), image_path)
        pos = self.image_finder_pyautogui.find_image(abs_path)
        
        if pos:
            pg.click(pos[0], pos[1])
            time.sleep(1)
            return True
        return False

    def _process_image(self, menu_name, frame, menu_data):
        """이미지 처리 및 클릭 실행"""
        image_path = menu_data[frame]
        if image_path:
            abs_path = os.path.join(os.path.dirname(self.data_file), image_path)
            
            while self.running.get(menu_name, False):
                pos = self.image_finder_pyautogui.find_image(abs_path)
                if pos:
                    pg.click(pos[0], pos[1])
                    self.completed_frames[menu_name] += 1
                    break
                time.sleep(1)
                

    def start_macro(self, menu_name):
        """매크로 시작"""
        self.data = json.load(open(self.data_file, 'r', encoding='utf-8'))
        menu_data = self.data[menu_name]['other_values']
        
        button_state = self.data[menu_name]['other_values']['button_state']
        if button_state == 'off':
            print(f"[{menu_name}] 매크로가 off 상태입니다")
            return
        
        if not self.running.get(menu_name, False):
            self.running[menu_name] = True
            self.completed_frames[menu_name] = 0
            self.frame1_detected[menu_name] = False
            
            self.macro_threads[menu_name] = threading.Thread(
                target=self._run_macro, 
                args=(menu_name,)
            )
            print(f"\n[{menu_name}] 매크로가 시작되었습니다")
            if menu_name in ['menu2', 'menu3']:
                print(f"[{menu_name}] 배달 설정시간 : {menu_data['entry1']}\n"
                      f"[{menu_name}] 포장 설정시간 : {menu_data['entry2']}", flush=True)
            else:
                print(f"[{menu_name}] 배차 설정시간 : {menu_data['entry1']}")
            self.macro_threads[menu_name].daemon = True
            self.macro_threads[menu_name].start()

    def stop_macro(self, menu_name):
        """매크로 중지"""
        # 매크로가 실행 중이 아닐 때
        if not self.running.get(menu_name, False):
            print(f"\n[{menu_name}] 매크로가 실행중이 아닙니다\n")
            return
        
        # 매크로가 실행 중일 때
        self.running[menu_name] = False
        self.completed_frames[menu_name] = 0
        self.frame1_detected[menu_name] = False
        
        if menu_name in self.macro_threads:
            self.macro_threads[menu_name].join(timeout=1.0)
            del self.macro_threads[menu_name]
        
        # frame1_order에서 해당 메뉴 제거
        if menu_name in self.frame1_order:
            self.frame1_order.remove(menu_name)
        
        print(f"\n[{menu_name}] 매크로가 중지되었습니다")
        
        if not any(self.running.values()):
            print("모든 매크로가 중지되었습니다.\n")

    def adjust_time(self, menu_name, menu_data):
        """시간 조정"""
        while self.running.get(menu_name, False):
            pos, filename = self.image_finder_pyautogui.find_time_images(menu_name, menu_data)
            
            # entry1이 50인 경우 (SKIP)
            if pos is False and filename == "SKIP":
                break
            
            # pos가 None이거나 튜플이 아닌 경우 처리 (이미지를 찾지 못한 경우)
            if pos is None or filename is None or not isinstance(pos, tuple):
                time.sleep(1)
                continue
            
            # 기본값 설정
            repeat = abs(menu_data['entry1'] - 50) // 5
            
            

            # 이미지를 찾았고 repeat > 0인 경우
            for _ in range(repeat):
                try:
                    pg.click(pos[0], pos[1])
                    time.sleep(1)
                except (TypeError, IndexError) as e:
                    print(f"클릭 실패: {e}")
                    break
            break  # 작업 완료 후 종료

        time.sleep(1)