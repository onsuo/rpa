"""
Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오

1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
2. 화면 중간 LEARN HTML 클릭
3. 상단 메뉴 중 HOW TO 클릭
4. 좌측 메뉴 중 Contact Form 메뉴 클릭
5. 입력란에 아래 값 입력
    First Name: 나도
    Last Name: 코딩
    Country: Canada
    Subject: 퀴즈 완료하였습니다.
    ※ 위 값들은 변수로 미리 저장해두세요
6. 5초 대기 후 Submit 버튼 클릭
7. 5초 대기 후 브라우저 종료
"""

import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.w3schools.com")

browser.find_element("link text", "Learn HTML").click()
# browser.find_element("link text", "HOW TO").click()
browser.find_element("xpath", '//*[@id="topnav"]//a[text()="HOW TO"]').click()
time.sleep(0.5)
# browser.find_element("link text", "Contact Form").click()
browser.find_element("xpath", '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()

fname = "나도"
lname = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element("xpath", '//input[@id="fname"]').send_keys(fname)
browser.find_element("xpath", '//input[@id="lname"]').send_keys(lname)
browser.find_element("xpath", f'//select[@id="country"]/option[text()="{country}"]').click()
browser.find_element("xpath", '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element("link text", "Submit").click()

time.sleep(5)
browser.quit()
