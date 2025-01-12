VIRTUAL_KEYS = {
    # 숫자
    **{str(i): str(i) for i in range(10)},
    
    # 알파벳 (A-Z)
    **{chr(i): chr(i) for i in range(65, 91)},
    
    # 기능키 (F1-F12)
    **{f'F{i}': f'Key.f{i}' for i in range(1, 13)},  # F1, F2, ... 형식으로 저장
    
    # 특수문자
    '`': 'grave',
    '-': 'minus',
    '=': 'equal',
    '[': 'bracketleft',
    ']': 'bracketright',
    '\\': 'backslash',
    ';': 'semicolon',
    "'": 'apostrophe',
    ',': 'comma',
    '.': 'period',
    '/': 'slash',
}

def get_key_list():
    """ComboBox에 표시할 키 리스트 반환"""
    # F1-F12 키를 자연스러운 순서로 정렬
    f_keys = [f'F{i}' for i in range(1, 13)]
    
    # 숫자 키 (0-9)
    num_keys = [str(i) for i in range(10)]
    
    # 나머지 키들 정렬 (특수문자, 알파벳)
    other_keys = sorted([k for k in VIRTUAL_KEYS.keys() 
                        if not k.startswith('F') and not k.isdigit()])
    
    return f_keys + num_keys + other_keys

def get_key_value(key):
    """키 문자열을 pynput 형식으로 변환"""
    return VIRTUAL_KEYS.get(key, key) 