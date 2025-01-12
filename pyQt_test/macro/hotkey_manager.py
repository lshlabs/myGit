from pynput import keyboard
from pynput.keyboard import Key, GlobalHotKeys

class HotkeyManager:
    def __init__(self, macro_controller):
        self.macro_controller = macro_controller
        self.hotkey_listeners = []  # 핫키 리스너들을 저장할 리스트 추가

    def register_hotkeys(self):
        """모든 메뉴의 핫키 등록"""
        hotkeys = {}  # GlobalHotKeys에 전달할 핫키 딕셔너리
        
        print("\n=== 핫키 등록 정보 ===")
        
        for menu in ['menu2', 'menu3', 'menu6']:
            print(f"\n[ {menu} ]")
            # 액티브 모드 핫키
            run_hotkey = self._create_active_hotkey(menu, 'run')
            stop_hotkey = self._create_active_hotkey(menu, 'stop')
            
            if run_hotkey:
                hotkeys[run_hotkey] = lambda m=menu: self.macro_controller.start_macro(m)
                print(f"자동모드 실행 핫키: {run_hotkey}")
            else:
                print("자동모드 실행 핫키: 설정 안됨")
            
            if stop_hotkey:
                hotkeys[stop_hotkey] = lambda m=menu: self.macro_controller.stop_macro(m)
                print(f"자동모드 중지 핫키: {stop_hotkey}")
            else:
                print("자동모드 중지 핫키: 설정 안됨")
            
            # 패시브 모드 핫키
            max_ps = 6 if menu == 'menu6' else 3
            for i in range(1, max_ps + 1):
                ps_hotkey = self._create_passive_hotkey(menu, i)
                if ps_hotkey:
                    hotkeys[ps_hotkey] = lambda m=menu, img=i: self.macro_controller.click_coordinate(m, img)
                    print(f"수동모드 핫키 {i}: {ps_hotkey}")
                else:
                    print(f"수동모드 핫키 {i}: 설정 안됨")
        
        print("\n==================")
        
        # GlobalHotKeys 리스너 생성 및 시작
        if hotkeys:
            listener = GlobalHotKeys(hotkeys)
            listener.start()
            self.hotkey_listeners.append(listener)

    def unregister_all_hotkeys(self):
        """모든 핫키 해제"""
        for listener in self.hotkey_listeners:
            listener.stop()
        self.hotkey_listeners.clear()
    def _create_active_hotkey(self, menu, action):
        """액티브 모드 핫키 생성"""
        settings = self.macro_controller.data[menu]['settings_active']
        
        combo_value = settings[f'combo_{action}_value']
        if not combo_value or combo_value == '0':
            return None
        
        modifiers = []
        if settings[f'check_ctrl{1 if action == "run" else 2}_state']:
            modifiers.append('<ctrl>')
        if settings[f'check_alt{1 if action == "run" else 2}_state']:
            modifiers.append('<alt>')
        if settings[f'check_shift{1 if action == "run" else 2}_state']:
            modifiers.append('<shift>')
        
        # 특수 키 처리
        key = combo_value.lower()
        if key.startswith('f') and key[1:].isdigit():  # F1-F12 키 처리
            key = f'<f{key[1:]}>'
        
        if modifiers:
            return f"{'+'.join(modifiers)}+{key}"
        return key

    def _create_passive_hotkey(self, menu, index):
        """패시브 모드 핫키 생성"""
        settings = self.macro_controller.data[menu]['settings_passive']
        
        combo_value = settings[f'combo_ps{index}_value']
        if not combo_value or combo_value == '0':
            return None
        
        modifiers = []
        if settings[f'check_ctrl{index+2}_state']:
            modifiers.append('<ctrl>')
        if settings[f'check_alt{index+2}_state']:
            modifiers.append('<alt>')
        if settings[f'check_shift{index+2}_state']:
            modifiers.append('<shift>')
        
        # 특수 키 처리
        key = combo_value.lower()
        if key.startswith('f') and key[1:].isdigit():  # F1-F12 키 처리
            key = f'<f{key[1:]}>'
        
        if modifiers:
            return f"{'+'.join(modifiers)}+{key}"
        return key
