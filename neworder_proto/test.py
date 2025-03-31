from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random

# 웹드라이버 자동 설치 및 서비스 생성
service = Service(ChromeDriverManager().install())

# 브라우저 옵션 설정
options = Options()

# 1. 사용자 에이전트 설정
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# 2. 자동화 플래그 제거 시도
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 3. 웹드라이버 생성
driver = webdriver.Chrome(service=service, options=options)

# 4. 쿠키 유지를 위한 설정
driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled": False})

# 안트토크 메인 페이지 접속
driver.get("https://www.anttalk.co.kr/Page/?Page=Main")
print("페이지 제목:", driver.title)

# 페이지 로드 대기
time.sleep(2)

try:
    # 로그인 버튼 찾기 및 클릭
    login_button = driver.find_element(By.XPATH, "//*[@id=\"_TopQks\"]/a[3]")
    print("로그인 버튼 텍스트:", login_button.text)
    login_button.click()
    
    # 로그인 페이지 로드 대기
    time.sleep(2)
    
    # 네이버로 로그인 버튼 찾기 및 클릭
    # WebDriverWait를 사용하여 요소가 로드될 때까지 대기
    naver_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[13]/div/div/div/div/div[7]/a[2]"))
    )
    print("네이버 로그인 버튼 찾음")
    naver_login_button.click()
    
    # 네이버 로그인 페이지 로드 대기
    time.sleep(5)
    print("네이버 로그인 페이지 제목:", driver.title)
    
except Exception as e:
    print("오류 발생:", str(e))

# 브라우저는 바로 닫히지 않도록 잠시 대기
time.sleep(10)

# 브라우저 종료는 주석 처리하여 결과 확인 가능하게 함
# driver.quit()