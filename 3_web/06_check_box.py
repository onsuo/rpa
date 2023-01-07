import time

from selenium import webdriver

browser = webdriver.Chrome()
# browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame("iframeResult")

# elem = browser.find_element("xpath", '//*[@id="vehicle1"]')
elem = browser.find_element("id", "vehicle1")

if elem.is_selected() is False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택되어 있으므로 아무 것도 안함")

time.sleep(5)

if elem.is_selected() is False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택되어 있으므로 아무 것도 안함")

browser.quit()
