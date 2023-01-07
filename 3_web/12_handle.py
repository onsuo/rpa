import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")

curr_handle = browser.current_window_handle
print(curr_handle)  # 현재 윈도우 핸들 정보

# Try it yourself
browser.find_element("xpath", '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles  # 모든 핸들 정보
for handle in handles:
    print(handle)  # 각 핸들 정보
    browser.switch_to.window(handle)  # 각 핸들로 이동해서
    print(browser.title)  # 현재 핸들 (브라우저) 의 제목 표시
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행...

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)  # HTML input type="radio"
time.sleep(2)

# 브라우저 컨트롤이 가능한지 확인
browser.get("https://daum.net")
time.sleep(2)
