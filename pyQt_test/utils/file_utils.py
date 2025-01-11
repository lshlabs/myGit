import os
import json

def get_data_file_path():
    """데이터 파일 경로 반환"""
    return os.path.join(os.path.dirname(__file__), 'data.json')

def load_json_data(file_path):
    """JSON 파일 로드"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_json_data(file_path, data):
    """JSON 파일 저장"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_relative_path(absolute_path):
    """절대 경로를 상대 경로로 변환"""
    if not absolute_path:
        return None
    try:
        return os.path.relpath(absolute_path, os.path.dirname(__file__))
    except ValueError:
        return absolute_path

def get_absolute_path(relative_path):
    """상대 경로를 절대 경로로 변환"""
    if not relative_path:
        return None
    return os.path.join(os.path.dirname(__file__), relative_path) 