from pathlib import Path
import json
import shutil
from PIL import Image

class DataManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        if DataManager._instance is not None:
            raise Exception("DataManager는 싱글톤 클래스입니다.")
        
        self.data_path = Path(__file__).parent / 'data.json'
        self.img_path = Path(__file__).parents[1] / 'img'
        self._data = self._load_data()
        DataManager._instance = self
    
    def _load_data(self):
        """데이터 로드"""
        default_data = {
            'macro_list': {},
            'settings_main': {
                'resolution': None,
                'custom': False
            }
        }
        
        try:
            if self.data_path.exists():
                with open(self.data_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 기존 매크로에 program 필드 추가
                    for macro in data.get('macro_list', {}).values():
                        if 'program' not in macro:
                            macro['program'] = None
                    return data
            return default_data
        except Exception as e:
            print(f"데이터 로드 중 오류 발생: {e}")
            return default_data
    
    def save_data(self):
        """데이터 저장"""
        try:
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"데이터 저장 중 오류 발생: {e}")
            return False
    
    def create_default_actions(self, macro_key):
        """기본 액션 생성"""
        macro_name = self._data['macro_list'][macro_key]['name']
        macro_folder = self.img_path / macro_name
        macro_folder.mkdir(exist_ok=True)
        
        # 기본 액션 생성
        actions = {}
        action_names = {
            'A0': '- 버튼 이미지',
            'A1': '+ 버튼 이미지',
            'A2': '예상시간 이미지',
            'A3': '거부버튼 이미지',
            'A4': '접수버튼 이미지'
        }
        
        for key, name in action_names.items():
            actions[key] = {
                'name': name,
                'type': 'image',
                'number': int(key[1]) + 1,
                'image': str(macro_folder / f'{key}.png'),
                'surface': [1],
                'priority': False
            }
            
        self._data['macro_list'][macro_key]['actions'] = actions
        return self.save_data()
        
    def save_cropped_images(self, macro_key, original_image, drag_areas):
        """드래그 영역으로 이미지 크롭하여 저장"""
        macro_name = self._data['macro_list'][macro_key]['name']
        macro_folder = self.img_path / macro_name
        macro_folder.mkdir(exist_ok=True)
        
        # PIL Image로 변환
        img = Image.open(original_image)
        
        # 각 영역별 이미지 크롭 및 저장
        area_files = {
            'minus': 'A0.png',
            'plus': 'A1.png',
            'time': 'A2.png',
            'reject': 'A3.png',  # 거절버튼
            'accept': 'A4.png'   # 수락버튼
        }
        
        for area_name, filename in area_files.items():
            if area_name in drag_areas and drag_areas[area_name]:
                rect = drag_areas[area_name]
                cropped = img.crop((rect.x(), rect.y(), 
                                  rect.x() + rect.width(), 
                                  rect.y() + rect.height()))
                cropped.save(macro_folder / filename)
                
        return True
    
    def create_delay_action(self, macro_key, delay_time):
        """딜레이 액션 생성"""
        try:
            actions = self._data['macro_list'][macro_key]['actions']
            # 새로운 액션 번호 계산
            new_number = len(actions) + 1
            new_key = f'A{len(actions)}'
            
            # 딜레이 액션 생성
            actions[new_key] = {
                'name': f'딜레이: {delay_time}초',
                'type': 'delay',
                'number': new_number,
                'value': float(delay_time),
                'priority': False
            }
            
            return self.save_data()
        except Exception as e:
            print(f"딜레이 액션 생성 중 오류 발생: {e}")
            return False
    
    def create_image_action(self, macro_key, name, image_path, surfaces):
        """이미지 액션 생성"""
        try:
            actions = self._data['macro_list'][macro_key]['actions']
            
            # 새로운 액션 키 생성 (마지막 번호 + 1)
            last_num = -1
            for key in actions.keys():
                if key.startswith('A'):
                    try:
                        num = int(key[1:])
                        last_num = max(last_num, num)
                    except ValueError:
                        continue
            new_key = f'A{last_num + 1}'
            
            # 새로운 number 계산 (현재 가장 큰 number + 1)
            new_number = max([action['number'] for action in actions.values()], default=0) + 1
            
            # 새로운 액션 생성
            actions[new_key] = {
                'name': name,
                'type': 'image',
                'number': new_number,
                'image': str(image_path),
                'surface': surfaces,
                'priority': False
            }
            
            return new_key
            
        except Exception as e:
            print(f"이미지 액션 생성 중 오류 발생: {e}")
            return None
    
    def copy_macro(self, original_macro_key, new_name):
        """매크로 복제
        
        Args:
            original_macro_key (str): 원본 매크로 키
            new_name (str): 새로운 매크로 이름
            
        Returns:
            str: 새로운 매크로 키
        """
        try:
            # 새로운 매크로 키 생성 (수정된 부분)
            macro_keys = self._data['macro_list'].keys()
            next_num = 1
            while f"M{next_num}" in macro_keys:
                next_num += 1
            new_macro_key = f"M{next_num}"
            
            # 원본 매크로 데이터 복사
            original_macro = self._data['macro_list'][original_macro_key]
            new_macro = {
                'name': new_name,
                'program': original_macro.get('program'),
                'actions': {}
            }
            
            # 액션 데이터 복사
            for action_key, action_data in original_macro['actions'].items():
                new_macro['actions'][action_key] = action_data.copy()
            
            # 이미지 파일 복사
            original_folder = self.img_path / original_macro['name']
            new_folder = self.img_path / new_name
            if original_folder.exists():
                # 기존 폴더가 있다면 삭제
                if new_folder.exists():
                    shutil.rmtree(new_folder)
                # 폴더 복사
                shutil.copytree(original_folder, new_folder)
                
                # 이미지 경로 업데이트
                for action in new_macro['actions'].values():
                    if action['type'] == 'image':
                        old_path = Path(action['image'])
                        action['image'] = str(new_folder / old_path.name)
            
            # 새로운 매크로 저장
            self._data['macro_list'][new_macro_key] = new_macro
            self.save_data()
            
            return new_macro_key
            
        except Exception as e:
            print(f"매크로 복제 중 오류 발생: {e}")
            return None
    
    def create_wizard_actions(self, macro_key, temp_manager):
        """액션 위자드로 새로운 액션 5개 생성
        
        Args:
            macro_key (str): 매크로 키
            temp_manager (TempManager): 임시 이미지 관리자
            
        Returns:
            bool: 성공 여부
        """
        try:
            actions = self._data['macro_list'][macro_key]['actions']
            macro_name = self._data['macro_list'][macro_key]['name']
            macro_folder = self.img_path / macro_name
            
            # 새로운 액션 키와 번호 계산
            last_key_num = -1
            for key in actions.keys():
                if key.startswith('A'):
                    try:
                        num = int(key[1:])
                        last_key_num = max(last_key_num, num)
                    except ValueError:
                        continue
                    
            # 새로운 number는 현재 가장 큰 number + 1부터
            new_number = max([action['number'] for action in actions.values()], default=0) + 1
            
            # 새로운 액션 생성
            area_files = {
                'minus': ('- 버튼 이미지', f'A{last_key_num + 1}.png'),
                'plus': ('+ 버튼 이미지', f'A{last_key_num + 2}.png'),
                'time': ('예상시간 이미지', f'A{last_key_num + 3}.png'),
                'reject': ('거부버튼 이미지', f'A{last_key_num + 4}.png'),
                'accept': ('접수버튼 이미지', f'A{last_key_num + 5}.png')
            }
            
            # 이미지 복사 및 액션 생성
            for i, (label, (name, filename)) in enumerate(area_files.items()):
                temp_image_path = temp_manager.get_cropped_image(label)
                if temp_image_path:
                    # 이미지 복사
                    shutil.copy2(temp_image_path, macro_folder / filename)
                    
                    # 액션 생성
                    action_key = f'A{last_key_num + i + 1}'
                    actions[action_key] = {
                        'name': name,
                        'type': 'image',
                        'number': new_number + i,
                        'image': str(macro_folder / filename),
                        'surface': [1],
                        'priority': False
                    }
            
            return self.save_data()
            
        except Exception as e:
            print(f"액션 위자드로 액션 생성 중 오류 발생: {e}")
            return False