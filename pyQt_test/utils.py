# pyQt_test/utils.py
import os
import json

def get_project_root():
    """프로젝트 루트 경로 반환"""
    return os.path.dirname(os.path.abspath(__file__))

def get_data_file_path():
    """data.json 파일의 경로 반환"""
    return os.path.join(get_project_root(), 'data.json')

def get_relative_path(absolute_path):
    """절대 경로를 상대 경로로 변환"""
    try:
        current_dir = get_project_root()
        relative_path = os.path.relpath(absolute_path, current_dir)
        return relative_path.replace(os.path.sep, '/')
    except ValueError:
        return absolute_path

def get_absolute_path(relative_path):
    """상대 경로를 절대 경로로 변환"""
    if not relative_path:
        return None
    relative_path = relative_path.replace('/', os.path.sep)
    return os.path.join(get_project_root(), relative_path)

def load_json_data(file_path):
    """JSON 파일 읽기"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("데이터 파일을 찾을 수 없습니다.")
    except json.JSONDecodeError:
        print("JSON 파일 형식이 잘못되었습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
    return None

def save_json_data(file_path, data):
    """JSON 파일 쓰기"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
        return False