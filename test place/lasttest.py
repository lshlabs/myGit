import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import easyocr
import cv2
import re  # 정규표현식 사용을 위한 import
import numpy as np
import time  # 실행시간 측정을 위한 import

def recognize_text(image_path):
    """이미지에서 특정 키워드만 인식하고 중심 좌표와 함께 반환"""
    start_time = time.time()  # 시작 시간 기록
    reader = easyocr.Reader(['ko'], gpu=True)  # 한글만 인식, GPU 사용
    
    # 화이트리스트 (찾고자 하는 키워드 목록)
    whitelist_keywords = ['포장', '배달', '신규 주문', '주문 접수']
    # 블랙리스트 (제외할 키워드 목록)
    blacklist_keywords = ['별도포장', '포장 준비 시간', '배달 시간']
    
    # 시간 패턴 정규식
    time_pattern = r'\d{1,2}분'
    
    # 이미지 로드 및 크기 조정
    image = cv2.imread(image_path)
    if image is None:
        print("이미지를 읽을 수 없습니다.")
        return []
    
    # 이미지 크기를 더 작게 조정
    width = 400  # 800에서 400으로 축소
    scale = width / image.shape[1]
    height = int(image.shape[0] * scale)
    image = cv2.resize(image, (width, height))
    
    # ROI 설정 (상단 30%만 처리)
    roi_height = int(height * 1)
    roi = image[0:roi_height, :]
    
    # 이미지 전처리 최적화
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # OCR 처리 최적화 - paragraph=False로 변경
    results = reader.readtext(gray,
                            paragraph=False,  # False로 변경
                            min_size=20,
                            width_ths=0.5,
                            contrast_ths=0.1,
                            text_threshold=0.6,
                            low_text=0.3)
    
    filtered_results = []
    found_keywords = set()
    app_type = None
    time_found = None
    
    for result in results:
        bbox, text, prob = result  # 이제 올바르게 언패킹됨
        text = text.strip()
        
        # 블랙리스트 키워드가 포함된 경우 건너뛰기
        if any(blackword in text for blackword in blacklist_keywords):
            continue
            
        # 앱 타입 확인
        if '신규 주문' in text:
            app_type = '배민'
        elif '주문 접수' in text:
            app_type = '요기요'
            
        # 배달/포장 키워드 확인
        if '포장' in text and '포장' in whitelist_keywords:
            found_keywords.add('포장')
        if '배달' in text and '배달' in whitelist_keywords:
            found_keywords.add('배달')
            
        # 시간 패턴 확인
        time_match = re.search(time_pattern, text)
        if time_match:
            time_found = time_match.group()
    
    # 결과 메시지 출력
    delivery_type = []
    if '포장' in found_keywords:
        delivery_type.append("포장")
    if '배달' in found_keywords:
        delivery_type.append("배달")
    
    if delivery_type and app_type:
        delivery_str = "/".join(delivery_type)
        if time_found:
            print(f"\n{app_type} {delivery_str} : {time_found} 설정되었음")
        else:
            print(f"\n{app_type} {delivery_str}입니다.")
    elif delivery_type:
        delivery_str = "/".join(delivery_type)
        if time_found:
            print(f"\n{delivery_str} : {time_found} 설정되었음")
        else:
            print(f"\n{delivery_str}입니다.")
    
    # 실행 시간 계산 및 출력
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"실행 시간: {execution_time:.2f}초")
    
    return found_keywords

if __name__ == "__main__":
    image_path = "/Users/mac/Documents/GitHub/myGit/test place/요기요 포장.png"
    results = recognize_text(image_path)