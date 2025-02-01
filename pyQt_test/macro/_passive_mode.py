import time
import pyautogui
from pynput.mouse import Controller as MouseController, Button
from pynput import keyboard
from utils.file_utils import load_json_data

class PassiveMode:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.mouse = MouseController()
        self.keyboard_controller = keyboard.Controller()
        self.last_click_time = 0  # 마지막 클릭 시간 저장
        self.click_delay = 0.5    # 클릭 간 최소 간격 (초)

    def click_coordinate(self, menu, image_num):
        """특정 메뉴의 이미지 좌표 클릭"""
        current_time = time.time()
        if current_time - self.last_click_time < self.click_delay:
            return  # 마지막 클릭으로부터 일정 시간이 지나지 않았으면 무시
            
        try:
            data = load_json_data(self.data_file)
            menu_data = data.get(menu, {})
            
            if not self._is_macro_enabled(menu_data, menu):
                return
            
            x, y = self._get_coordinates(menu_data, image_num)
            if x and y:
                # 핫키(특히 Ctrl)가 떼질 때까지 충분히 대기
                time.sleep(0.3)  # 사용자가 키를 뗄 때까지 대기
                # self._release_modifier_keys()  # 혹시 모를 modifier keys 해제
                self._click(x, y, menu, image_num)
                self.last_click_time = current_time  # 클릭 시간 업데이트
            
        except Exception as e:
            print(f"좌표 클릭 중 오류 발생: {e}")

    # def _release_modifier_keys(self):
    #     """modifier keys 해제"""
    #     modifier_keys = [keyboard.Key.ctrl, keyboard.Key.alt, keyboard.Key.shift]
    #     for key in modifier_keys:
    #         self.keyboard_controller.release(key)

    def _is_macro_enabled(self, menu_data, menu):
        """매크로 활성화 상태 확인"""
        if not menu_data:
            print("데이터가 유효하지 않습니다.")
            return False
            
        if menu_data['other_values']['button_state'] == 'off':
            print(f"[{menu}] 매크로가 off 상태입니다")
            return False
            
        if not menu_data['mode']['radio_passive_state']:
            print(f"[{menu}] 수동모드가 아닙니다")
            return False
            
        return True

    def _get_coordinates(self, menu_data, image_num):
        """좌표 가져오기"""
        try:
            coordinates = menu_data['coordinates_passive']['setting_pos']
            x = coordinates[f'image{image_num}_x']
            y = coordinates[f'image{image_num}_y']
            
            return (x, y) if x != 0 and y != 0 else (None, None)
        except KeyError:
            return None, None

    def _click(self, x, y, menu, image_num):
        """좌표 클릭 실행"""
        pyautogui.click(x, y)
        print(f"{menu}의 이미지{image_num} 좌표({x}, {y}) 클릭 완료")