import pyautogui

pyautogui.sleep(3)  # 3초 대기
print(pyautogui.position())

pyautogui.click(227, 60, duration=1)  # 1초 동안 (64, 17) 좌표로 이동 후 마우스 클릭
pyautogui.click()  # mouseDown + mouseUp
pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.doubleClick()
pyautogui.click(clicks=500)

pyautogui.moveTo(200, 300)
pyautogui.mouseDown()  # 마우스 버튼 누름
pyautogui.moveTo(300, 500)
pyautogui.mouseUp()  # 마우스 버튼 뗌

pyautogui.rightClick()
pyautogui.middleClick()

pyautogui.moveTo(995, 184)
pyautogui.drag(100, 0)  # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그
pyautogui.drag(100, 0, duration=0.25)  # 너무 빠른 동작으로 drag 수행이 안될 때는 duration 설정
pyautogui.dragTo(1095, 184, duration=0.25)  # 절대 좌표 기준으로 드래그

pyautogui.scroll(300)  # 양수이면 위 방향으로, 음수이면 아래 방향으로 300 만큼 스크롤
