from PIL import ImageGrab, Image
import numpy as np
import cv2
import time 
from ahk import AHK
import threading 

newImg = cv2.imread('imgs/NN/save.png')

for i in range(6):

    # crop the image to one of each door
    crop_img = newImg[0:150, (i*120) + 20:((i+1)*120) - 20]
    
    cv2.imwrite('imgs/NN/{}.png'.format(i),crop_img)