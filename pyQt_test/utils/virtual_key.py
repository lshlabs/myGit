VIRTUAL_KEYS = {
    # 숫자
    **{str(i): str(i) for i in range(10)},
    
    # 알파벳 (A-Z)
    **{chr(i): chr(i) for i in range(65, 91)},
    
    # 기능키 (F1-F12), F10 제외
    **{f'F{i}': f'Key.f{i}' for i in range(1, 13) if i != 10},  # F10 제외
    
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
    """가상 키 리스트 반환"""
    # VIRTUAL_KEYS의 키들을 정렬하여 반환
    return sorted(VIRTUAL_KEYS.keys(), key=lambda x: (
        # F키는 숫자 부분으로 정렬, 숫자가 없으면 0으로 처리
        int(x[1:]) if x.startswith('F') and x[1:].isdigit() else 
        # 나머지는 문자 자체로 정렬
        ord(x) if len(x) == 1 else ord(x[0])
    ))

def get_key_value(key):
    """키 문자열을 pynput 형식으로 변환"""
    return VIRTUAL_KEYS.get(key, key) 