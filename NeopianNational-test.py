from PIL import ImageGrab, Image
import numpy as np
import cv2
import time 
from ahk import AHK

ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')


# Full Screen
X_START = 410
Y_START = 350
X_STOP = 1110
Y_STOP = 500

FOUND = []
counter = 0
COUNTER_THRESH = 10
USE_FOUND = True

RED_MIN = np.array([0, 0, 190], np.uint8)
RED_MAX = np.array([100, 100, 255], np.uint8)
RAC_MIN = np.array([35, 75, 110], np.uint8)
RAC_MAX = np.array([65, 105, 150], np.uint8)
GH_MIN = np.array([0, 100, 85], np.uint8)
GH_MAX = np.array([10, 150, 120], np.uint8)

def presskey(index):
    if (index == 0):
        ahk.key_press('s')
    elif (index == 1):
        ahk.key_press('d')
    elif (index == 2):
        ahk.key_press('f')
    elif (index == 3):
        ahk.key_press('j')
    elif (index == 4):
        ahk.key_press('k')
    elif (index == 5):
        ahk.key_press('l')

def checkForBaddies(i, partOfImg):
    # Check for snek
    dst = cv2.inRange(partOfImg, RED_MIN, RED_MAX)
    no_red = cv2.countNonZero(dst)
    if (no_red > 1000):
        print("snek found at {}, red: {}, count: {}".format(i, no_red, counter))
        if (USE_FOUND): FOUND.append(i)
        presskey(i)

    # Check for raccoon
    dst = cv2.inRange(partOfImg, RAC_MIN, RAC_MAX)
    no_rac = cv2.countNonZero(dst)
    if (no_rac > 400):
        print("rac found at {}, rac: {}, count: {}".format(i, no_rac, counter))
        if (USE_FOUND): FOUND.append(i)
        presskey(i)

    # Check for greenhorn
    dst = cv2.inRange(partOfImg, GH_MIN, GH_MAX)
    no_gh = cv2.countNonZero(dst)
    if (no_gh > 150):
        print("greenhorn found at {}, green: {}, count: {}".format(i, no_gh, counter))
        if (USE_FOUND): FOUND.append(i)
        presskey(i)


def main():
    global FOUND, USE_FOUND, counter, COUNTER_THRESH
    while True:

        # Save part of the screen where game is
        im=ImageGrab.grab(bbox=(X_START,Y_START,X_STOP,Y_STOP))
        img = np.array(im)
        counter += 1

        if (USE_FOUND and counter % COUNTER_THRESH == 0):
            FOUND.clear()

        for i in range(6):
            if (i in FOUND): continue

            # crop the image to one of each door
            crop_img = img[0:150, (i*120) + 20:((i+1)*120) - 20]
            
            img2 = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
            # cv2.imwrite('imgs/{}.png'.format(i),img2)

            checkForBaddies(i, img2)
main()