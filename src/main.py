import pyautogui
import time
import keyboard
import mouseclick


def main_quest(x, y):
    main = pyautogui.locateOnScreen(
        'static/main_quest_arrow.png', region=(x, y, 30, 28), grayscale=True, confidence=0.85)
    if main == None:
        print("growing")
        time.sleep(0.5)
    else:
        print("stop")
        mouseclick.click(x, y)
        time.sleep(0.5)


def left_shift(x, y):
    avoidance = pyautogui.locateOnScreen(
        'static/avoidance.png', region=(x, y, 95, 95), grayscale=True, confidence=0.8)
    if avoidance != None:
        print("avoidance")
        mouseclick.click(x+40, y+40)
    else:
        time.sleep(0.5)


while keyboard.is_pressed('q') == False:
    left_shift(1300, 600)
