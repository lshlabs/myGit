# 이 코드는 [ 전체화면 > 부분화면 > 색상검사 > 앱 감지 ] 로직을 통해 배민과 요기요를 구분함
import cv2
import numpy as np
import time
import pyautogui

def detect_app_by_icon(image):
    # 결과 시각화를 위한 이미지 복사
    visualization = image.copy()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 마스크 생성 및 픽셀 계산
    red_mask = cv2.bitwise_or(
        cv2.inRange(hsv, np.array([0, 150, 100]), np.array([10, 255, 255])),
        cv2.inRange(hsv, np.array([170, 150, 100]), np.array([180, 255, 255]))
    )
    mint_mask = cv2.inRange(hsv, np.array([85, 100, 100]), np.array([95, 255, 255]))
    
    red_pixels = cv2.countNonZero(red_mask)
    mint_pixels = cv2.countNonZero(mint_mask)
    
    # 간단한 시각화
    visualization[red_mask > 0] = [0, 0, 255]
    visualization[mint_mask > 0] = [0, 255, 128]
    
    # 픽셀 수만 간단히 표시 (검은색 테두리와 함께 노란색 텍스트)
    text = f'R:{red_pixels} M:{mint_pixels}'
    # 검은색 테두리
    cv2.putText(visualization, text, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 4)
    # 노란색 텍스트
    cv2.putText(visualization, text, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    # 결과 판단 (임계값 미세 조정)
    if red_pixels > 1000:
        return "요기요", visualization
    elif mint_pixels > 2000:
        return "배민", visualization
    return "알 수 없음", visualization

if __name__ == "__main__":
    # 스크린 크기 출력은 한 번만
    screen = pyautogui.size()
    actual_width = screen.width
    actual_height = screen.height
    print(f"실제 화면 크기: {actual_width}x{actual_height}")
    
    # 고정 좌표 설정
    x1, y1 = 1232, 537
    x2, y2 = 1677, 939
    
    print(f"분석 영역 좌표: ({x1}, {y1}) ~ ({x2}, {y2})")
    
    print("\n3초 후에 스크린샷을 촬영합니다...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # 전체 화면 스크린샷
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Retina 디스플레이 스케일링 적용
    x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
    
    # 지정된 영역 추출
    roi = screenshot[y1:y2, x1:x2]
    
    # 앱 감지
    result, vis_roi = detect_app_by_icon(roi)
    print(f"\n감지된 앱: {result}")
    
    # 스케일링된 좌표로 사각형 그리기
    cv2.rectangle(screenshot, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # 원본 좌표값과 감지 결과 텍스트 표시
    cv2.putText(screenshot, f'({x1//2},{y1//2})', (x1, y1-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(screenshot, f'({x2//2},{y2//2})', (x2+10, y2), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(screenshot, f'Detected: {result}', (x1, y1-30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # 실제 화면 크기로 리사이즈
    resized_screenshot = cv2.resize(screenshot, (actual_width, actual_height))
    
    # 결과 영역 별도 창으로 표시
    cv2.imshow('Selected Region', vis_roi)
    cv2.imshow('Screenshot with Selected Region', resized_screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()