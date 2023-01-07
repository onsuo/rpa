import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"download.default_directory": r"C:\Dev\rpa"})

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame("iframeResult")

# download 링크 클릭
elem = browser.find_element("xpath", "/html/body/p[2]/a")
elem.click()

time.sleep(5)
