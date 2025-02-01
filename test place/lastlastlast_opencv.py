import cv2
import numpy as np
import time
import pyautogui

def find_template_matching(template_path, screenshot, x1, y1, x2, y2):
    # 템플릿 이미지 로드
    template = cv2.imread(template_path)
    
    # 지정된 영역 추출
    roi = screenshot[y1:y2, x1:x2]
    
    print(f"ROI 크기: {roi.shape[:2]}")
    print(f"템플릿 크기: {template.shape[:2]}")
    
    # 템플릿 매칭 수행
    # TM_CCOEFF_NORMED 방법이 크기나 밝기 변화에 강함
    result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
    
    # 임계값 이상의 매칭 위치 찾기
    threshold = 0.8
    locations = np.where(result >= threshold)
    
    # 결과 시각화
    roi_with_box = roi.copy()
    
    if len(locations[0]) > 0:  # 매칭이 하나라도 있으면
        # 템플릿 크기
        h, w = template.shape[:2]
        
        for pt in zip(*locations[::-1]):  # x,y 순서로 변환
            # 찾은 위치에 직사각형 그리기
            cv2.rectangle(roi_with_box, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        
        # 매칭 점수 표시
        max_val = np.max(result)
        cv2.putText(roi_with_box, f'Match Score: {max_val:.2f}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return True, roi_with_box
    
    return False, roi

if __name__ == "__main__":
    # 스크린 크기 출력
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
    
    # UI 템플릿 매칭
    template_path = "/Users/mac/Documents/GitHub/myGit/test place/요기요 배달 (2).png"
    found, vis_roi = find_template_matching(template_path, screenshot, x1, y1, x2, y2)
    
    # 스케일링된 좌표로 사각형 그리기
    cv2.rectangle(screenshot, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # 원본 좌표값과 감지 결과 텍스트 표시
    cv2.putText(screenshot, f'({x1//2},{y1//2})', (x1, y1-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(screenshot, f'({x2//2},{y2//2})', (x2+10, y2), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(screenshot, f'Template Found: {found}', (x1, y1-30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # 실제 화면 크기로 리사이즈
    resized_screenshot = cv2.resize(screenshot, (actual_width, actual_height))
    
    # 결과 표시
    cv2.imshow('Selected Region', vis_roi)
    cv2.imshow('Screenshot with Selected Region', resized_screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()