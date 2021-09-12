from pyautogui import *
import time
import pyautogui
import pytesseract
import cv2

outputNameFish = ""
outputSizeFish = ""
nameFish = pyautogui.screenshot(region=(650,100,270,200))
nameFish.save(r"C:\restaurant-project\fish.png")
SizeFish = pyautogui.screenshot(region=(650,360,270,100))
SizeFish.save(r"C:\restaurant-project\price.png")
pytesseract.pytesseract.tesseract_cmd = 'C:\\tesseract\\tesseract.exe'
time.sleep(1)

imgNameFish = cv2.imread('fish.png')
imgSizeFish = cv2.imread('price.png')

imgNameFish = cv2.cvtColor(imgNameFish, cv2.COLOR_BGR2RGB)
imgSizeFish = cv2.cvtColor(imgSizeFish, cv2.COLOR_BGR2RGB)

resultNameFish = pytesseract.image_to_string(imgNameFish)
resultSizeFish = pytesseract.image_to_string(imgSizeFish)

splitedNameFish = resultNameFish.split()
splitedSizeFish = resultSizeFish.split()

for i in range(0, len(splitedNameFish)):
    outputNameFish = outputNameFish + str(splitedNameFish[i]) + " "
print(outputNameFish)
for i in range(0, len(splitedSizeFish)):
    outputSizeFish = outputSizeFish + str(splitedSizeFish[i]) + " "
print(outputSizeFish)
cv2.imshow('result', imgNameFish)
cv2.waitKey(0)
cv2.imshow('result', imgSizeFish)
cv2.waitKey(0)