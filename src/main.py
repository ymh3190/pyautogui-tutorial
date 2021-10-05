import pyautogui
import time
import keyboard


MAIN = "main"
state = None
region = (950, 90, 780, 860)


def equip():
    (screen, x, y) = get_screen('equip')
    if screen != None:
        print("장착")
        pyautogui.click(x, y)


def move():
    (screen, x, y) = get_screen('paid_move')
    if screen != None:
        print("유료 이동")
        pyautogui.click(x, y)

    (screen, x, y) = get_screen('free_move')
    if screen != None:
        print("무료 이동")
        pyautogui.click(x, y)


def fast_move():
    (screen, x, y) = get_screen('fast_move')
    if screen != None:
        print("빠른 이동")
        pyautogui.click(x, y)
        time.sleep(0.1)
        move()


def proceed():
    (screen, x, y) = get_screen('proceed_arrow')
    if screen != None:
        global state
        state = None
        pyautogui.click(x, y)


def receive_reward():
    (screen, x, y) = get_screen('receive_reward')
    if screen != None:
        print("보상 수령")
        global state
        state = None
        pyautogui.click(x, y)


def skip():
    (screen, x, y) = get_screen('skip')
    if screen != None:
        print("스킵")
        global state
        state = None
        pyautogui.click(x, y)


def clear_main_quest():
    (screen, x, y) = get_screen('clear_check')
    if screen != None:
        print("메인퀘스트 클리어")
        global state
        state = None
        pyautogui.click(x, y)


def start_main_quest():
    (screen, x, y) = get_screen('main_quest_arrow')
    if screen != None:
        print("메인퀘스트 시작")
        global state
        state = MAIN
        pyautogui.click(x, y)
        fast_move()


def left_shift():
    (screen, x, y) = get_screen('avoidance')
    if screen != None:
        print("회피스킬 사용")
        pyautogui.click(x, y)


def get_screen(filename):
    screen = pyautogui.locateOnScreen(
        f'static/{filename}.png', region=region, grayscale=True, confidence=0.8)
    if screen:
        return (screen, screen.left+10, screen.top+10)


while keyboard.is_pressed('q') != True:
    # left_shift()
    if state != MAIN:
        start_main_quest()
    clear_main_quest()
    skip()
    receive_reward()
    proceed()
    time.sleep(0.5)
