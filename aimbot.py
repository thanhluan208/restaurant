from pyautogui import *
import time
import pyautogui


pyautogui.FAILSAFE = False
first_time = True
fishing = False
while 1:
    while fishing or first_time:
        time.sleep(0.05)
        pic = pyautogui.screenshot( region=(0,260,800,330))

        width, height = pic.size
        count = 0
        check = 0
        for x in range( 0, width, 5):
            for y in range(0, height, 5):

                r,g,b = pic.getpixel((x,y))

                if r == 255 and g == 255 and b == 255:
                    check += 1
        print(check)
        if check in range (320,400):
            time.sleep(0.5)
            click(780,378)
        if check in range (290,310) or check == 271:
            click(940,367)
            time.sleep(1)
            click(704,91)
            time.sleep(1)
            click(746,317)
            time.sleep(1)
            click(488,459)
            time.sleep(1)
            click(488,459)
            time.sleep(1)
            click(949,107)
            time.sleep(1)
            click(780,378)
            time.sleep(1)
        if check in range (37,50):
            print(check)
            print("checked")
            sleep(1)
            for x in range( 0, width, 5):
                for y in range(0, height, 5):

                    r,g,b = pic.getpixel((x,y))

                    if r == 14 and g == 24 and b == 59:
                        count = count + 1
                    elif r == 14 and g == 38 and b == 70:
                        count = count + 1
                    elif r == 0 and g == 97 and b == 140:
                        count = count + 1
                    elif r == 104 and g == 84 and b == 111:
                        count = count + 1
            check = 0
            first_time = False
            print(count)
            if count < 15 and count != 0:
                click(861,488)
                time.sleep(0.5)
                click(706,485)
                time.sleep(0.5)
                click(787,508)
                time.sleep(0.5)
                click(780,378)
                fishing = True
                print("small fish") 
                break   
            if count > 100:
                fishing = False
                print("big fish !!!")
                break
            else:
                print("normal fish") 
                fishing = False
                break
        if check > 300 and check < 320:
            fishing = False
            first_time = False
            break
    while not fishing:
        fish = pyautogui.screenshot( region=(0,0,800,200))

        width, height = fish.size
        detect = 0
        for x in range( 0, width, 5):
            for y in range(0, height, 5):

                r,g,b = fish.getpixel((x,y))

                if r == 255 and g == 255 and b == 255:
                    detect += 1
        print("detect: {}".format(detect))
        if detect in range (22,30) and check != 23:
            click(861,488)
            time.sleep(4)
            click(706,485)
            time.sleep(0.5)
            click(787,508)
            time.sleep(0.5)
            click(780,378)
            fishing = True
            break
        
