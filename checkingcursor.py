import pyautogui
import time

print(pyautogui.size())
time.sleep(8)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)