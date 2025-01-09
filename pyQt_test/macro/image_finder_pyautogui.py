import os
import cv2
import numpy as np
from PIL import ImageGrab
from datetime import datetime

class ImageFinder:
    def __init__(self):
        # macOS의 Retina 디스플레이 대응
        if os.name != 'nt':  # macOS
            screenshot = ImageGrab.grab()
            self.screen_scale = 2  # Retina 디스플레이의 경우 2배 스케일
        else:  # Windows
            self.screen_scale = 1
            
        # 디버그 이미지 저장 디렉토리 생성
        self.debug_dir = './debug_images_opencv'
        os.makedirs(self.debug_dir, exist_ok=True)

    def save_debug_image(self, img, prefix):
        """디버그용 이미지 저장"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{prefix}_{timestamp}.png"
        filepath = os.path.join(self.debug_dir, filename)
        
        if isinstance(img, np.ndarray):
            cv2.imwrite(filepath, img)
        else:
            img.save(filepath)
        print(f"디버그 이미지 저장됨: {filepath}\n", flush=True)
        return filepath

    def find_time_images(self, menu_name, menu_data):
        """시간 조정 이미지 검색 및 조정 방향 결정"""
        # 먼저 entry1 값 체크
        if menu_data['entry1'] == 50:
            print(f"[{menu_name}] 배달시간 조정이 필요하지 않습니다.\n")
            return False, "SKIP"
        
        image_folder = "pyQt_test/img/"
        
        try:
            # menu2는 배민, menu3는 요기요 이미지 검색
            if menu_name == 'menu2':
                d_path = os.path.join(image_folder, 'd_baemin.png')
                d_pos = self.find_image(d_path)
                
                if d_pos:  # 배민 배달 이미지 발견
                    button_img = 'plus_baemin.png' if menu_data['entry1'] > 50 else 'minus_baemin.png'
                    button_path = os.path.join(image_folder, button_img)
                    #print(f"[{menu_name}] 배달 시간 조정")
                    button_pos = self.find_image(button_path)
                    return button_pos, button_img
                
            elif menu_name == 'menu3':
                d_path = os.path.join(image_folder, 'd_yogiyo.png')
                d_pos = self.find_image(d_path)
                
                if d_pos:  # 요기요 배달 이미지 발견
                    button_img = 'plus_yogiyo.png' if menu_data['entry1'] > 50 else 'minus_yogiyo.png'
                    button_path = os.path.join(image_folder, button_img)
                    #print(f"[{menu_name}] 배달 시간 조정")
                    button_pos = self.find_image(button_path)
                    return button_pos, button_img

            return None, None  # 이미지를 찾지 못한 경우

        except Exception as e:
            print(f"find_time_images 오류: {e}")
            return None, None

    def find_image(self, image_path):
        """OpenCV를 사용한 이미지 검색"""
        try:
            # 일반적인 이미지 검색 로직
            screenshot = np.array(ImageGrab.grab())
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
            template = cv2.imread(image_path)
            
            if template is None:
                print(f"이미지를 로드할 수 없습니다: {image_path}")
                return None
            
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            threshold = 0.8
            if max_val >= threshold:
                h, w = template.shape[:2]
                center_x = max_loc[0] + w/2
                center_y = max_loc[1] + h/2
                
                print(f"타겟 이미지 찾음: {os.path.basename(image_path)}")
                # 디버그용 시각화
                cv2.rectangle(screenshot, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
                self.save_debug_image(screenshot, 'result')
                
                return (center_x/self.screen_scale, center_y/self.screen_scale)
                
            return None
                
        except Exception as e:
            print(f"이미지 검색 실패: {e}")
            return None