from pyautogui import *
import time
import pyautogui
import keyboard
from win32gui import FindWindow, GetWindowRect
import win32gui



pyautogui.FAILSAFE = False
fishing = True
snap = 0
snap_fish = []

print("Điền tên giả lập: ")
windowName = input()
print("Điền loại cần câu:")
rodtype = int(input())

def getWindowPosAndSize(windowName):
    fishing_process=[]
    window_handle = FindWindow(None, windowName)
    window_rect   = GetWindowRect(window_handle)
    for i in range(0,4):
        fishing_process.append(window_rect[i])
    return fishing_process


def checkFish(fishing_process):
    screenShot = pyautogui.screenshot(region=(fishing_process[0],fishing_process[1],fishing_process[2],fishing_process[3]))
    width, height = screenShot.size 
    fish_check = 0
    for x in range( 0, width, 5):
            for y in range(0, height, 5):
                r,g,b = screenShot.getpixel((x,y))
                if r == 14 and g == 24 and b == 59:
                    fish_check = fish_check + 1
                elif r == 14 and g == 38 and b == 70:
                    fish_check = fish_check + 1
                elif r == 0 and g == 97 and b == 140:
                    fish_check = fish_check + 1
                elif r == 104 and g == 84 and b == 111:
                    fish_check = fish_check + 1
    return fish_check

def fixRod(fishing_process, rodtype):
    click(round(fishing_process[2]/1.4),round(fishing_process[3]/6.3))
    time.sleep(1)
    click(round(fishing_process[2]/1.04),round(fishing_process[3]/1.65))
    time.sleep(1)
    click(round(fishing_process[2]/1.65 + round(fishing_process[2]/6.38)*rodtype),round(fishing_process[3]/1.86))
    time.sleep(1)
    click(round(fishing_process[2]/2.15),round(fishing_process[3]/1.31))
    time.sleep(1)
    click(round(fishing_process[2]/2.15),round(fishing_process[3]/1.31))
    time.sleep(1)
    click(round(fishing_process[2]/1.13), round(fishing_process[3]/5,7))
    time.sleep(1)
    click(round(fishing_process[2]/1.37),round(fishing_process[3]/1.6))

def getFish(fishing_process):
    click(round(fishing_process[2]/1.14),round(fishing_process[3]/1.256))
    while pyautogui.locateOnScreen("store.png", confidence=0.7) == None:
        if pyautogui.locateOnScreen("detected5.png", region=(fishing_process[0],fishing_process[1],fishing_process[2],fishing_process[3]),grayscale=True, confidence=0.7) != None or pyautogui.locateOnScreen("detected3.png", region=(fishing_process[0],fishing_process[1],fishing_process[2],fishing_process[3]),grayscale=True, confidence=0.7) != None or pyautogui.locateOnScreen("detected6.png", region=(fishing_process[0],fishing_process[1],fishing_process[2],fishing_process[3]),grayscale=True, confidence=0.7) != None :
            break
    click(round(fishing_process[2]/1.5),round(fishing_process[3]/1.224))
    time.sleep(1)
    click(round(fishing_process[2]/1.36),round(fishing_process[3]/1.2))
    time.sleep(1)
    click(round(fishing_process[2]/1.26),round(fishing_process[3]/1.58))

while True:
    count = 0 
    fishing_process = getWindowPosAndSize(windowName)
    check = checkFish(fishing_process)
    if check > 0 : 
        print(check)
        time.sleep(1)
        fishSize = checkFish(fishing_process)
        # if fishSize > fishing_process[2]/49.35: 
        if fishSize > fishing_process[2]/49.35:
            print("normalfish")
            print(fishSize)
            while True:
                print(count)
                if pyautogui.locateOnScreen("detected1.png",region=(0,0,800,400),grayscale=True, confidence=0.8) != None:
                    getFish(fishing_process)
                    break
               
        if fishSize == 0:
            continue
        else:
            print(fishSize)
            print("smallfish")
            click(round(fishing_process[2]/1.14),round(fishing_process[3]/1.256))
            time.sleep(1)
            click(round(fishing_process[2]/1.26),round(fishing_process[3]/1.58))
    if pyautogui.locateOnScreen("detected4.png",grayscale=True, confidence=15) != None:
        fixRod(fishing_process, rodtype)
    if keyboard.is_pressed('q'):
        break


