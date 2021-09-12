from pyautogui import *
import time
import pyautogui
import keyboard
from win32gui import FindWindow, GetWindowRect
import win32gui



pyautogui.FAILSAFE = False
fishing = True
snap = 0
count = 0
snap_fish = []

def getWindowPosAndSize():
    fishing_process=[]
    windowName = input()
    window_handle = FindWindow(None, windowName)
    window_rect   = GetWindowRect(window_handle)
    for i in range(0,4):
        fishing_process.append(window_rect[i])
    return fishing_process

fishing_process = getWindowPosAndSize()
print(fishing_process)
click(round(fishing_process[2]/2.15),round(fishing_process[3]/1.31))
# print(fishing_process[2]/462,fishing_process[3]/259)
# def checkFish(fishing_process):
#     screenShot = pyautogui.screenshot(region=(fishing_process[0],fishing_process[1],fishing_process[2],fishing_process[3]))
#     width, height = screenShot.size 
#     fish_check = 0
#     for x in range( 0, width, 5):
#             for y in range(0, height, 5):
#                 r,g,b = screenShot.getpixel((x,y))
#                 if r == 14 and g == 24 and b == 59:
#                     click(fishing_process[2]/1.4,)
#                 elif r == 14 and g == 38 and b == 70:
#                     fish_check = fish_check + 1
#                 elif r == 0 and g == 97 and b == 140:
#                     fish_check = fish_check + 1
#                 elif r == 104 and g == 84 and b == 111:
#                     fish_check = fish_check + 1
#     return fish_check
