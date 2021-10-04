from collections import namedtuple
import threading
from numpy import string_
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import mouseclick
from threading import Thread


def main_quest(x, y):
    main = pyautogui.locateOnScreen(
        'static/main_quest_arrow.png', region=(x, y, 30, 28), grayscale=True, confidence=0.85)
    if main == None:
        print("growing")
        time.sleep(0.5)
    else:
        print("stop")
        mouseclick.click(x+10, y+10)
        time.sleep(0.5)


def left_shift(x, y):
    avoidance = pyautogui.locateOnScreen(
        'static/avoidance.png', region=(x, y, 95, 95), grayscale=True, confidence=0.8)
    if avoidance == None:
        print("unavoidance")
        time.sleep(0.5)
    else:
        print("avoidance")
        mouseclick.click(x, y)
        time.sleep(0.5)


if __name__ == "__main__":
    while True:
        thread_avoidance = Thread(target=left_shift, args=(1340, 630))
        # thread_avoidance.start()
        # thread_avoidance.join()

        thread_main = Thread(target=main_quest, args=(1402, 190))
        thread_main.start()
        thread_main.join()
