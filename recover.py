from PIL.ImageOps import grayscale
from pyautogui import *
import time
import pyautogui
import pyttsx3
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\tesseract\\tesseract.exe'

# outputNameFish = ""
# outputSizeFish = ""

# AiSpeak = pyttsx3.init()
# AiSpeak.setProperty('rate', 160)
# AiBrain = ""

# goFishing = "lets go fishing"
# t = time.localtime()
# current_time = time.strftime("%H", t)
# print(current_time)

# if int(current_time) >= 0 and int(current_time) < 12: AiSpeak.say("Goodmorning Sir!" + goFishing)
# elif int(current_time) >= 12 and int(current_time) <= 17: AiSpeak.say("Goodafternoon Sir!" + goFishing)
# else : AiSpeak.say("Goodevening Sir" + goFishing)
# AiSpeak.runAndWait()

# time.sleep(1)



while 1:
    if pyautogui.locateOnScreen("detected.png", region=(0,0,800,300),grayscale=True, confidence=0.6) != None:
        click(861,488)
        time.sleep(4)
        nameFish = pyautogui.screenshot(region=(650,80,270,60))
        nameFish.save(r"C:\restaurant-project\fish.png")
        SizeFish = pyautogui.screenshot(region=(650,360,270,100))
        SizeFish.save(r"C:\restaurant-project\price.png")

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
        if outputNameFish == " Old Doll ": outputNameFish = "Gabbage Gabbage Gabbage !!"
        AiSpeak.say(outputNameFish)
        AiSpeak.runAndWait()
        print(outputNameFish)
        
        for i in range(0, len(splitedSizeFish)):
            outputSizeFish = outputSizeFish + str(splitedSizeFish[i]) + " "
        AiSpeak.say(outputSizeFish)
        AiSpeak.runAndWait()
        print(outputSizeFish)

        click(715,520)
        time.sleep(0.5)
        click(787,508)
        time.sleep(0.5)
        click(780,378)
    
    # elif pyautogui.locateOnScreen("detected.png", region=(0,0,800,400),grayscale=True, confidence=0.9) != None  :
    #     click(861,488)
    #     time.sleep(4)
        # nameFish = pyautogui.screenshot(region=(650,80,270,100))
        # nameFish.save(r"C:\restaurant-project\fish.png")
        # SizeFish = pyautogui.screenshot(region=(650,360,270,100))
        # SizeFish.save(r"C:\restaurant-project\price.png")

        # imgNameFish = cv2.imread('fish.png')
        # imgSizeFish = cv2.imread('price.png')

        # imgNameFish = cv2.cvtColor(imgNameFish, cv2.COLOR_BGR2RGB)
        # imgSizeFish = cv2.cvtColor(imgSizeFish, cv2.COLOR_BGR2RGB)

        # resultNameFish = pytesseract.image_to_string(imgNameFish)
        # resultSizeFish = pytesseract.image_to_string(imgSizeFish)

        # splitedNameFish = resultNameFish.split()
        # splitedSizeFish = resultSizeFish.split()

        # for i in range(0, len(splitedNameFish)):
        #     outputNameFish = outputNameFish + str(splitedNameFish[i]) + " "
        # AiSpeak.say(outputNameFish)
        # AiSpeak.runAndWait()
        # for i in range(0, len(splitedSizeFish)):
        #     outputSizeFish = outputSizeFish + str(splitedSizeFish[i]) + " "
        # AiSpeak.say(outputSizeFish)
        # AiSpeak.runAndWait()

        # click(715,520)
        # time.sleep(0.5)
        # click(787,508)
        # time.sleep(0.5)
        # click(780,378)
    elif pyautogui.locateOnScreen("detected2.png", region=(0,0,800,400),grayscale=True, confidence=0.5) != None or  pyautogui.locateOnScreen("detected4.png", region=(0,0,800,400),grayscale=True, confidence=0.5) != None  :
        # AiSpeak.say("fishing rod is broken")
        # AiSpeak.runAndWait()
        click(940,367)
        time.sleep(2)
        click(706,113)
        time.sleep(2)
        click(598,327)
        time.sleep(2)
        click(488,459)
        time.sleep(2)
        click(488,459)
        time.sleep(2)
        click(949,107)
        time.sleep(2)
        click(780,378)
        time.sleep(2)
        # AiSpeak.say("fishing rod is repaired !")
        # AiSpeak.runAndWait()
    # outputNameFish = ""
    # outputSizeFish = ""
  
    