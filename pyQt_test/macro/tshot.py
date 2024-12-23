import pyautogui as pg
import os

# 스크린샷을 저장할 경로 설정
screenshot_path = './screenshot/test_screenshot.png'

# 디렉토리 존재 여부 확인 및 생성
if not os.path.exists(os.path.dirname(screenshot_path)):
    os.makedirs(os.path.dirname(screenshot_path))

# 스크린샷 찍기
try:
    pg.screenshot(screenshot_path)
    print(f"스크린샷이 성공적으로 저장되었습니다: {screenshot_path}")
except Exception as e:
    print(f"스크린샷 저장 실패: {e}")