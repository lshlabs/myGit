from pathlib import Path
import json
import shutil
from PIL import Image

class TempManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        if TempManager._instance is not None:
            raise Exception("TempManager는 싱글톤 클래스입니다.")
            
        self.temp_dir = Path(__file__).parents[1] / 'temp'
        self.temp_dir.mkdir(exist_ok=True)
        self.temp_path = self.temp_dir / 'tempdata.json'
        self._temp_data = self._load_temp_data()
        TempManager._instance = self
        
    def _load_temp_data(self):
        """임시 데이터 로드"""
        default_data = {
            'drag_areas': {
                'plus': None,
                'minus': None,
                'time': None,
                'accept': None,
                'reject': None
            },
            'temp_images': {
                'step2': None,  # 드래그 영역이 그려진 step2 이미지 경로
                'step3': None   # 드래그 영역이 그려진 step3 이미지 경로
            },
            'cropped_images': {
                'plus': None,
                'minus': None,
                'time': None,
                'accept': None,
                'reject': None
            }
        }
        
        try:
            if self.temp_path.exists():
                with open(self.temp_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return default_data
        except Exception as e:
            print(f"임시 데이터 로드 중 오류 발생: {e}")
            return default_data
            
    def save_temp_data(self):
        """임시 데이터 저장"""
        try:
            with open(self.temp_path, 'w', encoding='utf-8') as f:
                json.dump(self._temp_data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"임시 데이터 저장 중 오류 발생: {e}")
            return False
            
    def save_drag_areas(self, drag_areas):
        """드래그 영역 저장"""
        # 기존 데이터 유지하면서 업데이트
        current_areas = self._temp_data['drag_areas']
        
        for label, rect in drag_areas.items():
            current_areas[label] = {
                'x': rect.x(),
                'y': rect.y(),
                'width': rect.width(),
                'height': rect.height()
            } if rect else None
        
        return self.save_temp_data()
        
    def get_drag_areas(self):
        """드래그 영역 가져오기"""
        return self._temp_data['drag_areas']
        
    def save_temp_image(self, image, step):
        """수정된 이미지 저장"""
        image_path = self.temp_dir / f'temp_step{step}.png'
        image.save(str(image_path))
        self._temp_data['temp_images'][f'step{step}'] = str(image_path)
        return self.save_temp_data()
        
    def get_temp_image(self, step):
        """수정된 이미지 가져오기"""
        return self._temp_data['temp_images'][f'step{step}']
        
    def save_cropped_image(self, image, label):
        """크롭된 이미지 저장"""
        image_path = self.temp_dir / f'crop_{label}.png'
        image.save(str(image_path))
        self._temp_data['cropped_images'][label] = str(image_path)
        return self.save_temp_data()
        
    def get_cropped_image(self, label):
        """크롭된 이미지 가져오기"""
        return self._temp_data['cropped_images'][label]
        
    def clear_temp_data(self):
        """임시 데이터 초기화"""
        # 임시 파일들 삭제
        for path in self.temp_dir.glob('*.png'):
            path.unlink(missing_ok=True)
            
        if self.temp_path.exists():
            self.temp_path.unlink()
            
        self._temp_data = self._load_temp_data()