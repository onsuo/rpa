"""
<html>
    <body>
        <iframe id="1">
            <html>
                <body>
                    <div...>
                </body>
            </html>
        </iframe>
        <iframe id="2">
            <html>
                <body>
                    <div...>
                </body>
            </html>
        </iframe>
    </body>
</html>
"""

import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame("iframeResult")  # frame 전환

elem = browser.find_element(by="xpath", value='//*[@id="html"]')  # 성공
elem.click()

browser.switch_to.default_content()  # 상위로 빠져 나옴
# elem = browser.find_element(by="xpath", value='//*[@id="html"]')  # 실패
# elem.click()

time.sleep(5)
browser.quit()
