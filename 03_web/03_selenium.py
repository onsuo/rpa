import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome("./chromedriver")
browser = webdriver.Chrome()

browser.get("https://naver.com")

time.sleep(1)
elem = browser.find_element(By.LINK_TEXT, "카페")
print(elem)

print(elem.get_dom_attribute("href"))
print(elem.get_dom_attribute("class"))

elem.click()
browser.back()
browser.forward()

elem = browser.find_element(By.ID, "query")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_element(By.TAG_NAME, "a")
print(elem)
print(elem.get_dom_attribute("href"))

elems = browser.find_elements(By.TAG_NAME, "a")
for e in elems:
    e.get_dom_attribute("href")

browser.get("https://daum.net")

elem = browser.find_element(By.NAME, "q")
elem.send_keys("나도코딩")
elem.send_keys("나도코딩")
elem.send_keys("나도코딩")
elem.clear()
elem.send_keys("나도코딩")

elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
elem.click()
browser.save_screenshot("daum.png")
print(browser.page_source)
# browser.close()  # 현재 탭 종료
browser.quit()  # 모든 탭 종료
