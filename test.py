from PIL.ImageOps import grayscale
from pyautogui import *
import pyautogui
import time
time.sleep(2)
bag = pyautogui.locateOnScreen("bag.png",grayscale=True, confidence=0.5) 
click(bag.left,bag.top)
time.sleep(1)
tool = pyautogui.locateOnScreen("tool.png",grayscale=True, confidence=0.5)
click(tool.left,tool.top)
time.sleep(1)
repair = pyautogui.locateOnScreen("repair.png",grayscale=True, confidence = 0.5)
click(repair.left,repair.top)
time.sleep(1)
confirm = pyautogui.locateOnScreen("confirm.png",grayscale=True, confidence = 0.5)
click(confirm.left,confirm.top)
time.sleep(1)
click(confirm.left,confirm.top)


