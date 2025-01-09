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
        print(f"디버그 이미지 저장됨: {filepath}\n", flush=True)
        return filepath
    
    def find_time_images(self, menu_name):
        """특정 메뉴의 시간 조정 이미지만 검색"""
        image_folder = "pyQt_test/img/"
        # menu_name에 따른 검사할 이미지 파일명 설정
        target_images = []
        if menu_name == 'menu2':  # 배민 메뉴
            target_images = ['d_time_baemin.png', 't_time_baemin.png']
        elif menu_name == 'menu3':  # 요기요 메뉴
            target_images = ['d_time_yogiyo.png', 't_time_yogiyo.png']

        for filename in os.listdir(image_folder):
            if filename in target_images:  # 해당 메뉴의 이미지만 검색
                image_path = os.path.join(image_folder, filename)
                pos, filename = self.find_image(image_path)
                if pos is not None:
                    return pos, filename
        return None, None

    def find_image(self, image_path=None, menu_name=None):
        """pyautogui를 사용한 이미지 검색"""
        if menu_name is not None:  # menu_name이 전달된 경우
            return self.find_time_images(menu_name)

        if image_path is not None:
            filename = os.path.basename(image_path)  # image_path가 None이 아닐 때만 파일 이름 추출
        else:
            print("이미지 경로가 제공되지 않았습니다.")
            return None, None  # 경로가 없을 경우 처리

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
                # 결과 이미지 저장
                print(f"\n타겟 이미지 찾음: {filename}")
                self.save_debug_image(screenshot_cv, 'result')
                
                return (click_x, click_y), filename
                
            else:
                return None, None
                
        except Exception as e:
            print(f"이미지 검색 실패: {e}")
            return None