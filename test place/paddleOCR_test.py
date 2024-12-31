import pyautogui
import cv2
from paddleocr import PaddleOCR
import numpy as np

# 화면 캡쳐
screenshot = pyautogui.screenshot()

# 캡쳐한 이미지를 OpenCV 형식으로 변환
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 이미지 파일로 저장 (선택 사항)
cv2.imwrite('screenshot.png', screenshot)

# PaddleOCR 초기화 (한글 인식)
ocr = PaddleOCR(use_angle_cls=True, lang='korean')

# 이미지에서 텍스트 인식
result = ocr.ocr('screenshot.png', cls=True)

# 결과 출력
for line in result:
    for word_info in line:
        print(word_info[1][0])  # 인식된 한글 텍스트 출력