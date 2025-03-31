from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 브라우저 설정
driver = webdriver.Chrome()
driver.get("https://www.anttalk.co.kr/Page/?Page=Coin&Cd=BTCUSDT")

# 로그인 (필요시)
# ...

# 매수 함수
def buy_coin(amount, leverage=10):
    # 레버리지 설정 (필요시)
    leverage_input = driver.find_element(By.ID, "여기에_레버리지_입력란_ID")
    leverage_input.clear()
    leverage_input.send_keys(str(leverage))
    
    # 수량 입력
    amount_input = driver.find_element(By.ID, "여기에_수량_입력란_ID")
    amount_input.clear()
    amount_input.send_keys(str(amount))
    
    # 매수 버튼 클릭
    buy_button = driver.find_element(By.CSS_SELECTOR, "여기에_매수버튼_선택자")
    buy_button.click()
    
    # 확인 버튼 (필요시)
    try:
        confirm_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "여기에_확인버튼_선택자"))
        )
        confirm_button.click()
    except:
        pass

# 매도 함수 (비슷한 방식으로 구현)