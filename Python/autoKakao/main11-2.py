import pyautogui
import pyperclip
import time
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pc1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pc2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pc3.png')
    print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~!")
    pyautogui.hotkey("ctrl","v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)