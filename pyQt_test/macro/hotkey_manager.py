from pynput.keyboard import Listener, Key, KeyCode
from utils.file_utils import load_json_data

class HotkeyManager:
    def __init__(self, active_mode, passive_mode, data_file):
        self.active_mode = active_mode
        self.passive_mode = passive_mode
        self.data_file = data_file
        self.current_keys = set()
        self.hotkeys = {}
        self.register_hotkeys()
        
        # 키보드 리스너 시작
        self.listener = Listener(
            on_press=self._on_press,
            on_release=self._on_release)
        self.listener.start()

    def register_hotkeys(self):
        """핫키 등록"""
        data = load_json_data(self.data_file)
        if not data:
            return

        # 기존 핫키 초기화
        self.hotkeys.clear()

        for menu in ['menu2', 'menu3', 'menu6']:
            settings = data[menu]['settings_active']
            
            # 실행/중지 핫키
            for action in ['run', 'stop']:
                ctrl = settings[f'check_ctrl{1 if action == "run" else 2}_state']
                alt = settings[f'check_alt{1 if action == "run" else 2}_state']
                shift = settings[f'check_shift{1 if action == "run" else 2}_state']
                key = settings[f'combo_{action}_value']
                
                if key and key != '0':
                    hotkey = (ctrl, alt, shift, key.lower())
                    func = self.active_mode.start_macro if action == 'run' else self.active_mode.stop_macro
                    self.hotkeys[hotkey] = lambda m=menu, f=func: f(m)
            
            # 패시브 모드 핫키
            settings = data[menu]['settings_passive']
            max_ps = 6 if menu == 'menu6' else 3
            for i in range(1, max_ps + 1):
                ctrl = settings[f'check_ctrl{i+2}_state']
                alt = settings[f'check_alt{i+2}_state']
                shift = settings[f'check_shift{i+2}_state']
                key = settings[f'combo_ps{i}_value']
                
                if key and key != '0':
                    hotkey = (ctrl, alt, shift, key.lower())
                    self.hotkeys[hotkey] = lambda m=menu, img=i: self.passive_mode.click_coordinate(m, img)

    def _on_press(self, key):
        """키가 눌렸을 때"""
        if key == Key.ctrl_l or key == Key.ctrl_r:
            self.current_keys.add('ctrl')
        elif key == Key.alt_l or key == Key.alt_r:
            self.current_keys.add('alt')
        elif key == Key.shift_l or key == Key.shift_r:
            self.current_keys.add('shift')
        elif isinstance(key, KeyCode):
            ctrl = 'ctrl' in self.current_keys
            alt = 'alt' in self.current_keys
            shift = 'shift' in self.current_keys
            
            # shift 키와 함께 눌린 문자 매핑
            shift_map = {
                '!': '1', '@': '2', '#': '3', '$': '4', '%': '5',
                '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'
            }
            
            if shift and key.char in shift_map:
                key_char = shift_map[key.char]
            else:
                key_char = key.char.lower() if key.char else None
            
            # 등록된 핫키와 비교
            for (h_ctrl, h_alt, h_shift, h_key), func in self.hotkeys.items():
                if (h_ctrl == ctrl and h_alt == alt and 
                    h_shift == shift and h_key == key_char):
                    func()
                    break

    def _on_release(self, key):
        """키가 떼졌을 때"""
        if key == Key.ctrl_l or key == Key.ctrl_r:
            self.current_keys.discard('ctrl')
        elif key == Key.alt_l or key == Key.alt_r:
            self.current_keys.discard('alt')
        elif key == Key.shift_l or key == Key.shift_r:
            self.current_keys.discard('shift')