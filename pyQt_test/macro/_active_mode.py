import json
import os
import time
import pyautogui
from .image_finder import ImageFinder
from .color_finder import ColorFinder
from collections import deque

class Cycle:
    def __init__(self, app_info):
        self.app_type = app_info[0]      # '배민' 또는 '요기요'
        self.order_type = app_info[1]    # '배달' 또는 '포장'
        self.current_step = 0
        self.is_emergency = True
        self.retry_count = 0             # 재시도 횟수

    def get_next_step(self):
        steps = {
            0: 'time_adjust',
            1: 'click_accept',
            2: 'click_manna_shortcut',
            3: 'click_app_accept',  # 배민접수 또는 요기요접수
            4: 'adjust_delivery_time',
            5: 'click_manna_accept'
        }
        return steps.get(self.current_step)

class ActiveMode:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.main_window = main_window
        self.image_finder = ImageFinder()
        self.color_finder = ColorFinder()
        self.cycle_queue = deque()
        self.current_cycle = None
        self.is_monitoring = False
        self.MAX_RETRIES = 10
        self.RETRY_INTERVAL = 3  # seconds
        
    def _load_data(self):
        """데이터 로드"""
        return json.load(open(self.data_file, 'r', encoding='utf-8'))
    
    def detect_app(self, x1, y1, x2, y2):
        """배민/요기요 구분"""
        return self.color_finder.find_color(x1, y1, x2, y2)
    
    def click_position(self, x, y, clicks=1):
        """지정된 좌표 클릭"""
        for _ in range(clicks):
            pyautogui.click(x, y)
            time.sleep(0.1)
    
    def find_and_click_image(self, menu_key, image_num):
        """이미지 찾아서 클릭"""
        data = self._load_data()
        menu_data = data[menu_key]
        
        image_path = menu_data['other_values'][f'frame_image{image_num}']
        if not image_path:
            print(f"이미지 경로가 설정되지 않음: {menu_key} - image{image_num}")
            return False
        
        x1 = menu_data['coordinates_active']['start_pos'][f'image{image_num}_x']
        y1 = menu_data['coordinates_active']['start_pos'][f'image{image_num}_y']
        x2 = menu_data['coordinates_active']['end_pos'][f'image{image_num}_x']
        y2 = menu_data['coordinates_active']['end_pos'][f'image{image_num}_y']
        
        pos = self.image_finder.find_image(image_path, x1, y1, x2, y2)
        if pos:
            self.click_position(pos[0], pos[1])
            return True
        return False

    def adjust_time(self, app_type, order_type):
        """배달/포장 시간 조정"""
        coords = None
        if app_type == '배민':
            coords = self.main_window.time_manager.get_baemin_coords()
        else:  # 요기요
            coords = self.main_window.time_manager.get_manna_coords()
            
        if coords and isinstance(coords, tuple):
            x, y = coords
            self.click_position(x, y)
            return True
        return False

    def adjust_delivery_time(self):
        """배차시간 조정"""
        coords = self.main_window.time_manager.get_manna_coords()
        if coords and isinstance(coords, tuple):
            x, y = coords
            self.click_position(x, y)
            return True
        return False

    def process_cycle(self, cycle):
        """단계별 사이클 처리"""
        menu_key = 'menu2' if cycle.app_type == '배민' else 'menu3'
        success = False
        
        if cycle.is_emergency:
            if cycle.current_step == 0:
                success = self.adjust_time(cycle.app_type, cycle.order_type)
            elif cycle.current_step == 1:
                success = self.find_and_click_image(menu_key, 1)  # 접수버튼
                if success:
                    cycle.is_emergency = False
        else:
            step = cycle.get_next_step()
            if step == 'click_manna_shortcut':
                success = self.find_and_click_image('menu6', 1)
            elif step == 'click_app_accept':
                # 배민/요기요 접수 (2번 또는 3번 이미지)
                image_num = 2 if cycle.app_type == '배민' else 3
                success = self.find_and_click_image('menu6', image_num)
            elif step == 'adjust_delivery_time':
                success = self.adjust_delivery_time()
            elif step == 'click_manna_accept':
                success = self.find_and_click_image('menu6', 4)

        if not success:
            cycle.retry_count += 1
            if cycle.retry_count >= self.MAX_RETRIES:
                print(f"이미지를 찾지 못했습니다. ({cycle.get_next_step()} 단계)")
                self.stop_macro()
                return True
            time.sleep(self.RETRY_INTERVAL)
            return False
        
        cycle.current_step += 1
        cycle.retry_count = 0
        return cycle.current_step >= 6

    def check_new_orders(self):
        """새로운 주문 확인"""
        if not self.is_monitoring:
            return
            
        data = self._load_data()
        for menu_name in ['menu2', 'menu3']:
            menu_data = data[menu_name]
            app_info = self.detect_app(
                menu_data['coordinates']['x1'],
                menu_data['coordinates']['y1'],
                menu_data['coordinates']['x2'],
                menu_data['coordinates']['y2']
            )
            
            if app_info and app_info[0] in ['배민', '요기요']:
                new_cycle = Cycle(app_info)
                self.cycle_queue.append(new_cycle)
    
    def start_monitoring(self):
        """모니터링 시작 (핫키로 호출)"""
        self.is_monitoring = True
        print("모니터링 시작")
        
    def stop_monitoring(self):
        """모니터링 중지 (핫키로 호출)"""
        self.is_monitoring = False
        print("모니터링 중지")
    
    def process_cycles(self):
        """사이클 처리"""
        while True:
            if self.is_monitoring:
                # 새로운 주문 확인
                self.check_new_orders()
                
                # 현재 사이클 처리
                if self.current_cycle:
                    if self.process_cycle(self.current_cycle):
                        if self.current_cycle.is_emergency:
                            # 긴급처리가 끝났으면 큐의 맨 뒤로
                            self.cycle_queue.append(self.current_cycle)
                        self.current_cycle = None
                
                # 새로운 사이클 시작
                elif self.cycle_queue:
                    self.current_cycle = self.cycle_queue.popleft()
            
            time.sleep(0.1)  # CPU 부하 방지
    
    def start_macro(self):
        """매크로 시작"""
        self.start_monitoring()
        self.process_cycles()
    
    def stop_macro(self):
        """매크로 중지"""
        self.stop_monitoring()
        self.current_cycle = None
        self.cycle_queue.clear()
        print("매크로가 중지되었습니다.")