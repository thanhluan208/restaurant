from pyautogui import *
import time
import pyautogui
import keyboard


pyautogui.FAILSAFE = False
first_time = True
fishing = False
while not keyboard.is_pressed("q"):
    while fishing or first_time:
        pic = pyautogui.screenshot( region=(0,200,800,300))

        width, height = pic.size
        count = 0
        check = 0
        for x in range( 0, width, 5):
            for y in range(0, height, 5):

                r,g,b = pic.getpixel((x,y))

                if r == 255 and g == 255 and b == 255:
                    check += 1
        if check in range (320,400):
            time.sleep(0.5)
            click(780,378)
        if check in range (240,320):
            pic.save("C:\\Users\\admin\\Desktop\\OpenCvBot\\saveimage.png")
            click(940,367)
            time.sleep(1)
            click(704,91)
            time.sleep(1)
            click(594,309)
            time.sleep(1)
            click(488,459)
            time.sleep(1)
            click(488,459)
            time.sleep(1)
            click(949,107)
            time.sleep(1)
            click(780,378)
            time.sleep(1)
        if check in range (5,100):
            sleep(1)
            for x in range( 0, width, 4):
                for y in range(0, height, 4):

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
            if count in range (0,40):
                print("fish size: {}".format(count))

                click(861,488)
                time.sleep(0.5)
                click(706,485)
                time.sleep(0.5)
                click(787,508)
                time.sleep(0.5)
                click(780,378)
                fishing = True
                break   
            if count > 100:
                fishing = False
                print("fish size: {}".format(count))
                print("lacoste !!!")
                break
            else:
                print("fish size: {}".format(count))
                pic.save("C:\\Users\\admin\\Desktop\\OpenCvBot\\saveimage.png")
                print("normal fish") 
                fishing = False
                break
        if check > 300 and check < 320:
            fishing = False
            first_time = False
            break
    while not fishing:
        fish = pyautogui.screenshot( region=(0,0,800,530))
        # fish.save("C:\\Users\\admin\\Desktop\\OpenCvBot\\fish.png")

        width, height = fish.size
        detect = 0
        for x in range( 0, width, 5):
            for y in range(0, height, 5):

                r,g,b = fish.getpixel((x,y))

                if r == 255 and g == 255 and b == 255:
                    detect += 1
        print(detect)
        if detect in range (20,30):
            click(861,488)
            time.sleep(8)
            click(706,485)
            time.sleep(0.5)
            click(787,508)
            time.sleep(0.5)
            click(780,378)
            fishing = True
            break
        if detect > 50:
            fishing = True
            break
