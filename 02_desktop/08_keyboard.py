# 참고) https://automatetheboringstuff.com/2e/chapter20/#:~:text=Table%2020%2D1%3A%20PyKeyboard%20Attributes

import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle("제목 없음")[0]  # 메모장 1개 띄운 상태에서 가져옴
w.activate()

pyautogui.write("12345")
pyautogui.write("NadoCoding", interval=0.25)
pyautogui.write("나도코딩")  # 한글 입력 불가

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, l a 순서대로 적고 enter 입력

# 특수 문자
# shift 4 -> $
pyautogui.keyDown("shift")  # shift 키를 누른 상태에서
pyautogui.press("4")  # 숫자 4를 입력하고
pyautogui.keyUp("shift")  # shift 키를 뗀다

# 조합키 (Hot Keys)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")  # press("a")
pyautogui.keyUp("ctrl")  # Ctrl + A

# 간편햔 조합키
pyautogui.hotkey("ctrl", "alt", "shit", "a")
# Ctrl 누름 > Alt 누름 > Shift 누름 > A 누름 > A 뗌 > Shift 뗌 > Alt 뗌 > Ctrl 뗌
pyautogui.hotkey("ctrl", "a")


pyperclip.copy("나도코딩")  # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")  # 클립보드에 있는 내용을 붙여넣기


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("나도코딩")

# 자동화 프로그램 종료
# win: ctrl + alt + del
# mac: cmd + shift + option + q
