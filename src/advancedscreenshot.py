from PIL.Image import register_open
import os
import pyautogui

""" 이미지크기보다 탐지하는 영역이 커야됨(당연히) """
im1 = pyautogui.screenshot(region=(1402, 190, 30, 28))
# im1.save(r'C:\Users\Administrator\Desktop\pyauto\static\savedimage.png')
# im1.save(os.getcwd()+"\savedimage.png")
im1.save(f"{os.getcwd()}\static\savedimage.png")

# 영역을 확인했으면 locationscreen에 region 인자값으로 줄것
