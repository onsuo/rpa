"""
Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오

1. 그림판 실행 (단축키: win + r, 입력값: mspaint) 및 최대화

2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
    - 입력 글자: "참 잘했어요"

3. 5초 대기 후 그림판 종료
    이때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함
"""

import sys

import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")  # pyautogui.write(["enter"])
pyautogui.sleep(1)
# paint = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
# if paint.isMaximized is False:
#     paint.maximize()

# pyautogui.press("t")
# pyautogui.click(x=480, y=450)
pyautogui.sleep(0.5)
btn_text = pyautogui.locateOnScreen("text.png")
if btn_text:
    pyautogui.click(btn_text)
else:
    print("찾기 실패")
    sys.exit()
pyautogui.click(btn_text.left - 200, btn_text.top + 300)
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)
# btn_close = pyautogui.locateOnScreen("close.png")
# pyautogui.click(btn_close)
pyautogui.hotkey("alt", "f4")
# pyautogui.sleep(1)
# btn_dont_save = pyautogui.locateOnScreen("dont_save.png")
# pyautogui.click(btn_dont_save)
pyautogui.press(["\t", "enter"])
