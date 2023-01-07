import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://flight.naver.com/")
time.sleep(1)

# 팝업 닫기
browser.find_element("xpath", '//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()
time.sleep(1)

# 가는 날 선택
browser.find_element("xpath", "//button[text()='가는 날']").click()
time.sleep(1)
browser.find_elements("xpath", "//b[text()='30']")[0].click()
# 오는 날
browser.find_elements("xpath", "//b[text()='5']")[1].click()

# 도착지 설정
browser.find_element("xpath", "//b[text()='도착']").click()
time.sleep(1)
browser.find_element("xpath", '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys(
    "제주"
)
time.sleep(1)
browser.find_element("xpath", "//i[text()='Jeju, Korea Republic of']").click()
time.sleep(1)

# 항공권 검색
browser.find_element("xpath", "//span[text()='항공권 검색']").click()

# 첫 번째 결과 출력

# 1: 실행 대기
time.sleep(10)
elem = browser.find_element("xpath", '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')
print(elem.text)  # element 내에 있는 text 출력

# 2: implicit wait
browser.implicitly_wait(10)
elem = browser.find_element("xpath", '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')
print(elem.text)

# 3: explicit wait
try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            ("xpath", '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')
        )
    )
    print(elem.text)
except NoSuchElementException:
    print("대상을 찾지 못했습니다.")

time.sleep(5)
