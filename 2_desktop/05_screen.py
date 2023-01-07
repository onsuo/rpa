import pyautogui

# 스크린 샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png")  # 파일로 저장

pyautogui.mouseInfo()
# 190,62 22,133,208 #1685D0

pixel = pyautogui.pixel(190, 62)
print(pixel)

print(pyautogui.pixelMatchesColor(190, 62, (22, 133, 208)))
print(pyautogui.pixelMatchesColor(190, 62, pixel))
print(pyautogui.pixelMatchesColor(190, 62, (22, 133, 209)))
