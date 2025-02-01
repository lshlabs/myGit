import threading
import pyautogui as pg
from .hotkey_manager import HotkeyManager
from ._active_mode import ActiveMode
from ._passive_mode import PassiveMode
from utils.file_utils import load_json_data

class MacroController:
    def __init__(self, data_file, main_window):
        self.data_file = data_file
        self.main_window = main_window
        
        # 모드 관리
        self.active_mode = ActiveMode(data_file, main_window)
        self.passive_mode = PassiveMode(data_file, main_window)
        
        # 핫키 매니저 초기화 및 등록
        self.hotkey_manager = HotkeyManager(
            active_mode=self.active_mode,
            passive_mode=self.passive_mode,
            data_file=self.data_file
        )
        self.hotkey_manager.register_hotkeys()

    def start_macro(self, menu_name):
        """매크로 시작"""
        data = load_json_data(self.data_file)
        
        # 매크로 on/off 상태 체크
        button_state = data[menu_name]['other_values']['button_state']
        if button_state == 'off':
            print(f"[{menu_name}] 매크로가 off 상태입니다")
            return
        
        # 모드에 따른 매크로 실행
        if data[menu_name]['mode']['radio_active_state']:
            self.active_mode.start_macro(menu_name)
        elif data[menu_name]['mode']['radio_passive_state']:
            self.passive_mode.start_macro(menu_name)

    def stop_macro(self, menu_name):
        """매크로 중지"""
        data = load_json_data(self.data_file)
        
        if data[menu_name]['mode']['radio_active_state']:
            self.active_mode.stop_macro(menu_name)