import pyautogui as pg
import os
import cv2
import numpy as np
from PIL import ImageGrab
from datetime import datetime

class ImageFinder:
    def __init__(self):
        if os.name != 'nt':
            self.screen_scale = pg.screenshot().size[0] / pg.size()[0]
        else:
            self.screen_scale = 1
            
        # 디버그 이미지 저장 디렉토리 생성
        self.debug_dir = './debug_images_pyautogui'
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
            
        print(f"\n디버그 이미지 저장됨: {filepath}\n")
        return filepath

    def find_image(self, image_path):
        """pyautogui를 사용한 이미지 검색"""
        try:
            # 현재 화면 스크린샷
            screenshot = ImageGrab.grab()
            
            # 타겟 이미지 로드
            target = cv2.imread(image_path)

            # pyautogui로 이미지 위치 찾기
            location = pg.locateOnScreen(
                image_path,
                confidence=0.8,
                grayscale=True
            )
            
            if location:
                # 결과 시각화
                screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                
                # 찾은 영역 표시
                x, y, w, h = location
                cv2.rectangle(
                    screenshot_cv,
                    (int(x), int(y)),
                    (int(x + w), int(y + h)),
                    (0, 255, 0),  # 녹색
                    2
                )
                
                # 중앙 점 표시
                center_x = x + (w / 2)
                center_y = y + (h / 2)
                cv2.circle(
                    screenshot_cv,
                    (int(center_x), int(center_y)),
                    5,
                    (0, 0, 255),  # 빨간색
                    -1
                )
                
                # 정보 텍스트 추가
                cv2.putText(
                    screenshot_cv,
                    f"Found at: ({int(center_x)}, {int(center_y)})",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )
                
                # # 결과 이미지 저장
                # self.save_debug_image(screenshot_cv, 'result')
                
                # 실제 클릭 좌표 계산
                click_x = center_x / self.screen_scale
                click_y = center_y / self.screen_scale
                
                print(f"\n타겟 이미지 찾음")
                # 결과 이미지 저장
                self.save_debug_image(screenshot_cv, 'result')
                
                return (click_x, click_y)
                
            else:
                return None
                
        except Exception as e:
            print(f"이미지 검색 실패: {e}")
            return None