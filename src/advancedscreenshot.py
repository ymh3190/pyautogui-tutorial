from PIL.Image import register_open
import os
import pyautogui

""" 이미지크기보다 탐지하는 영역이 커야됨(당연히) """
# img = pyautogui.screenshot(region=(1300, 600, 95, 95))  # 회피
# img = pyautogui.screenshot(region=(1395, 175, 45, 40)) # 메인퀘 시작
# img = pyautogui.screenshot(region=(1405, 192, 30, 22))
img = pyautogui.screenshot(region=(950, 90, 780, 860))
img.save(f"{os.getcwd()}\static\savedimage.png")
# img.save(r'C:\Users\Administrator\Desktop\pyauto\static\savedimage.png')
# img.save(os.getcwd()+"\savedimage.png")

# 영역을 확인했으면 locationscreen에 region 인자값으로 줄것
