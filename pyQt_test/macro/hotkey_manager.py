from pynput import keyboard

class HotkeyManager:
    def __init__(self, macro_controller):
       self.macro_controller = macro_controller
       self.hotkey_listener = None
    def create_hotkey_combination(self):
        """핫키 조합을 생성하는 메서드"""
        run_dict = {}
        stop_dict = {}
        
        # 각 메뉴에 대한 핫키 조합 생성
        for menu in ['menu2', 'menu3', 'menu6']:
            run_dict[menu] = self._create_hotkey(menu, 'run')
            stop_dict[menu] = self._create_hotkey(menu, 'stop')
        return run_dict, stop_dict
    
    def _create_hotkey(self, menu, action):
        """핫키 조합을 생성하는 헬퍼 메서드"""
        combo_value = self.macro_controller.data[menu]['settings'][f'combo_{action}_value']
        if not combo_value or combo_value == '0':
            return None
        
        parts = []
        # 수정자 키 확인
        if self.macro_controller.data[menu]['settings'][f'check_ctrl{1 if action == "run" else 2}_state']:
            parts.append('Key.ctrl')
        if self.macro_controller.data[menu]['settings'][f'check_alt{1 if action == "run" else 2}_state']:
            parts.append('Key.alt')
        if self.macro_controller.data[menu]['settings'][f'check_shift{1 if action == "run" else 2}_state']:
            parts.append('Key.shift')
        
        # 일반 키 추가
        parts.append(combo_value)
        
        # 핫키 문자열 생성 (예: 'Key.ctrl+1' 또는 그냥 '1')
        return '+'.join(parts)
    
    def register_hotkeys(self):
        """키보드 이벤트 리스너 등록"""
        run_combination, stop_combination = self.create_hotkey_combination()
        # 디버깅 출력
        print(f"menu2 실행 트리거 키 조합: {run_combination['menu2']}")
        print(f"menu2 종료 트리거 키 조합: {stop_combination['menu2']}")
        print(f"menu3 실행 트리거 키 조합: {run_combination['menu3']}")
        print(f"menu3 종료 트리거 키 조합: {stop_combination['menu3']}")
        print(f"menu6 실행 트리거 키 조합: {run_combination['menu6']}")
        print(f"menu6 종료 트리거 키 조합: {stop_combination['menu6']}")
        # 핫키 등록
        hotkey_dict = {
            run_combination['menu2']: lambda: self.macro_controller.start_macro('menu2'),
            stop_combination['menu2']: lambda: self.macro_controller.stop_macro('menu2'),
            run_combination['menu3']: lambda: self.macro_controller.start_macro('menu3'),
            stop_combination['menu3']: lambda: self.macro_controller.stop_macro('menu3'),
            run_combination['menu6']: lambda: self.macro_controller.start_macro('menu6'),
            stop_combination['menu6']: lambda: self.macro_controller.stop_macro('menu6')
        }
        # 빈 문자열 체크 및 핫키 등록
        self.hotkey_listener = keyboard.GlobalHotKeys({
            k: v for k, v in hotkey_dict.items() if k  # 빈 문자열이 아닌 경우만 등록
        })
        self.hotkey_listener.start()
        
        return hotkey_dict