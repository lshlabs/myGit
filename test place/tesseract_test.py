import cv2
import pytesseract
import re
import numpy as np

# Tesseract 실행 파일 경로 설정 (Mac의 경우)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Tesseract 설치 경로

def read_text_from_image(image_path):
    """이미지에서 숫자, 영문자, 한글을 읽어오는 함수"""
    print(f"이미지 경로: {image_path}")  # 디버깅: 이미지 경로 출력
    # 이미지 읽기
    image = cv2.imread(image_path)

    if image is None:
        print("이미지를 읽을 수 없습니다. 경로를 확인하세요.")  # 이미지 읽기 실패 시 메시지
        return ""

    # 이미지 전처리
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일로 변환
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Gaussian 블러 적용
    binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  # Adaptive Thresholding

    # Morphological Operations (침식)
    kernel = np.ones((3, 3), np.uint8)
    eroded_image = cv2.erode(binary_image, kernel, iterations=1)  # 글자 얇게 만들기

    # 이미지 출력
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Tesseract로 텍스트 인식
    custom_config = r'--oem 3 --psm 6 -l kor+eng'  # 한글과 영어 인식
    extracted_text = pytesseract.image_to_string(eroded_image, config=custom_config)

    # 특수문자 제외하고 숫자, 영문자, 한글만 출력
    filtered_text = re.sub(r'[^0-9a-zA-Z가-힣\s]', '', extracted_text)
    return filtered_text.strip()

# 이미지 경로 설정
image_path = '/Users/mac/Desktop/images9.png'  # 이미지 경로
extracted_text = read_text_from_image(image_path)

if extracted_text:
    print("추출된 텍스트:", extracted_text)
else:
    print("추출된 텍스트가 없습니다.")  # 텍스트가 없을 경우 메시지