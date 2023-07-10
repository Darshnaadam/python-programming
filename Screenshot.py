#  Taking Screenshot using pyautogui module

import pyautogui
screenshot = pyautogui.screenshot()
#takes screenshot of entire screen and saves it in the variable "screenshot"
screenshot.save('image1.png')
print("Screenshot is taken")