import cv2
import numpy as np
import pyautogui as pg
from PIL import ImageGrab
import os
from datetime import datetime

class ImageFinder:
    def __init__(self):
        # Mac 환경에서의 스케일링 팩터 설정
        if os.name != 'nt':  # Mac 환경인 경우
            self.screen_scale = pg.screenshot().size[0] / pg.size()[0]
        else:
            self.screen_scale = 1
            
        # 실제 화면 해상도
        self.real_width, self.real_height = pg.size()
        
        # 스크린샷 해상도 확인 (Retina 디스플레이 고려)
        screenshot = ImageGrab.grab()
        self.shot_width, self.shot_height = screenshot.size
        
        # 스케일 비율 계산 (screen_scale 반영)
        self.scale_x = (self.real_width * self.screen_scale) / self.shot_width
        self.scale_y = (self.real_height * self.screen_scale) / self.shot_height
        
        # ORB 검출기 초기화
        self.orb = cv2.ORB_create(nfeatures=1000)
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
        # 디버그 이미지 저장 디렉토리 생성
        self.debug_dir = './debug_images'
        os.makedirs(self.debug_dir, exist_ok=True)
        
        print(f"스크린 스케일: {self.screen_scale}")
        print(f"실제 화면 해상도: {self.real_width}x{self.real_height}")
        print(f"스크린샷 해상도: {self.shot_width}x{self.shot_height}")
        print(f"스케일 비율: ({self.scale_x}, {self.scale_y})")

    def save_debug_image(self, img, prefix):
        """디버그용 이미지 저장"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{prefix}_{timestamp}.png"
        filepath = os.path.join(self.debug_dir, filename)
        cv2.imwrite(filepath, img)
        print(f"디버그 이미지 저장됨: {filepath}")
        return filepath

    def find_image(self, image_path):
        """ORB를 사용한 이미지 검색"""
        try:
            # Mac에서 스크린샷 촬영
            screenshot = np.array(ImageGrab.grab())
            # RGB 스크린샷 저장
            rgb_path = self.save_debug_image(cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR), 'screenshot_rgb')
            
            # BGR로 변환
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
            # BGR 스크린샷 저장
            bgr_path = self.save_debug_image(screenshot, 'screenshot_bgr')

            # 타겟 이미지 로드 및 저장
            target = cv2.imread(image_path)
            if target is not None:
                target_path = self.save_debug_image(target, 'target')
            
            if target is None or screenshot is None:
                print("이미지 로드 실패")
                return None

            # 특징점 검출 및 디스크립터 계산
            kp1, des1 = self.orb.detectAndCompute(screenshot, None)
            kp2, des2 = self.orb.detectAndCompute(target, None)

            if des1 is None or des2 is None:
                print("특징점 검출 실패")
                return None

            # 특징점 매칭
            matches = self.bf.match(des2, des1)
            matches = sorted(matches, key=lambda x: x.distance)

            # 좋은 매칭점만 선택
            good_matches = matches[:15]
            if len(good_matches) < 5:
                print("충분한 매칭점 없음")
                return None

            # 매칭 결과 시각화
            match_img = cv2.drawMatches(target, kp2, screenshot, kp1, good_matches, None)
            match_path = self.save_debug_image(match_img, 'matches')

            # 매칭된 점들의 좌표 추출
            points = np.float32([kp1[m.trainIdx].pt for m in good_matches])
            
            # 중심점 계산 (스크린샷 좌표)
            center_x = np.mean(points[:, 0])
            center_y = np.mean(points[:, 1])

            # 중심점 표시한 이미지 저장
            result_img = screenshot.copy()
            cv2.circle(result_img, (int(center_x), int(center_y)), 10, (0, 255, 0), -1)
            result_path = self.save_debug_image(result_img, 'result')

            # 스크린샷 좌표를 실제 화면 좌표로 변환 (screen_scale 고려)
            real_x = (center_x / self.screen_scale)
            real_y = (center_y / self.screen_scale)

            print(f"스크린샷 좌표: ({center_x}, {center_y})")
            print(f"실제 화면 좌표: ({real_x}, {real_y})")
            print(f"스크린 스케일: {self.screen_scale}")

            return (real_x, real_y)
            
        except Exception as e:
            print(f"이미지 검색 중 오류 발생: {e}")
            return None