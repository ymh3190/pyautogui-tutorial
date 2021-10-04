# 게임 영역안 스크린샷을 찍고 5픽셀을 검사

from PIL.ImageOps import grayscale
import pyautogui
import time
import mouseclick

while True:
    # locateOnScreen: 이미지를 찾으면 left, top, width, height 값을 반환
    if pyautogui.locateOnScreen('static/main_quest_arrow.png', region=(1300, 600, 95, 95), grayscale=True, confidence=0.8) != None:
        print("find")
        mouseclick.click(1340, 630)
        time.sleep(0.5)
    else:
        print("not find")
        time.sleep(0.5)
