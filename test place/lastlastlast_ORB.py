import cv2
import numpy as np
import time
import pyautogui

def find_ui_template(template_path, screenshot, x1, y1, x2, y2):
    # 템플릿 이미지 로드
    template = cv2.imread(template_path)
    
    # 지정된 영역 추출
    roi = screenshot[y1:y2, x1:x2]
    
    # 그레이스케일 변환
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # ORB 검출기 생성
    orb = cv2.ORB_create(
        nfeatures=3000,
        scaleFactor=1.2,
        nlevels=8,
        edgeThreshold=15
    )
    
    # 특징점 검출 및 디스크립터 계산
    kp1, des1 = orb.detectAndCompute(template_gray, None)
    kp2, des2 = orb.detectAndCompute(roi_gray, None)
    
    if des2 is None:
        return False, roi
    
    # 특징점 매칭
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    
    # 좋은 매칭점만 필터링
    good_matches = sorted([m for m in matches if m.distance < 50], 
                         key=lambda x: x.distance)
    
    if len(good_matches) >= 15:
        # 매칭된 좌표 추출
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        
        # RANSAC으로 호모그래피 계산
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        
        if M is not None and mask is not None:
            # 매칭점들의 바운딩 박스 계산
            filtered_dst_pts = dst_pts[mask.ravel() == 1].reshape(-1, 2)
            
            if len(filtered_dst_pts) >= 4:  # 최소 4개의 점이 필요
                x_min = int(max(0, np.min(filtered_dst_pts[:, 0])))
                x_max = int(min(roi.shape[1], np.max(filtered_dst_pts[:, 0])))
                y_min = int(max(0, np.min(filtered_dst_pts[:, 1])))
                y_max = int(min(roi.shape[0], np.max(filtered_dst_pts[:, 1])))
                
                # ROI에 직사각형 그리기
                roi_with_box = roi.copy()
                cv2.rectangle(roi_with_box, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                
                # 매칭 결과 시각화
                result = cv2.drawMatches(template, kp1, roi, kp2, good_matches, None,
                                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                
                cv2.imshow('Matches', result)
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
    template_path = "/Users/mac/Documents/GitHub/myGit/test place/배민 배달 샘플.png"
    found, vis_roi = find_ui_template(template_path, screenshot, x1, y1, x2, y2)
    
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