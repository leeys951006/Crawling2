from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 경로 설정
chrome_driver_path = r'C:\Users\leeys\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe'

# Chrome 옵션 설정 (headless 모드)
chrome_options = Options()
chrome_options.add_argument("--headless")

# WebDriver 설정
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹사이트 URL
url = 'http://books.toscrape.com/'
driver.get(url)

# 페이지 제목 확인
print("Page title:", driver.title)

try:
    # <p> 태그로 데이터 추출
    wait = WebDriverWait(driver, 20)
    elements = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p'))
    )
    
    # 데이터 추출
    data = [element.text for element in elements]
    print("Extracted data:", data)
finally:
    # WebDriver 종료
    driver.quit()
