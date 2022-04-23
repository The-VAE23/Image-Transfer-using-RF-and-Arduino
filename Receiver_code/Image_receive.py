# Required Libraries

import keyboard
import serial
import time
import numpy as np
import cv2
from datetime import datetime
from functions import readSerial, printSerial


# Connecting with the Arduino
try:
    AR = serial.Serial(port='COM5', baudrate=9600, timeout=5)
    AR.close()
    AR.open()
    time.sleep(5)
    printSerial(AR)
except:
    print("Arduino Connection Failed")
    exit(0)

# Code to save image
def logimg():
    """Function that acquires img from the remote device"""
    # Variables to identify image shape
    imsize = (102240,230400,409920,921600,2073600,307200,480000,691200,786432,1228800,1470000,1555200,24300)
    imshape = ((240,426),(360,640),(480,854),(720,1280),(1080,1920),(480,640),(600,800),(720,960),(768,1024),(960,1280),(1050,1400),(1080,1440),(180,135))
    img = []
    while True:
        x=AR.inWaiting()
        if x>0:
            data = readSerial(AR).decode('utf-8')
            if data[0:-2] == "e":
                break
            else:
                img.append(int(data))
    img = np.array(img)
    i = imsize.index(img.size)
    img = img.reshape(imshape[i])
    img = img.astype(np.uint8)
    time_utc = datetime.now()
    time_utc = str(time_utc)[0:-7].replace(':',"").replace('-',"").replace(' ',"")
    cv2.imwrite("D:Data/"+time_utc+'.png', img)
    print("Image saved")

# Looping function that checks for available image and saves it
def loopfunc():
    x = AR.inWaiting()
    if x>0:
        data = readSerial(AR).decode('utf-8')
        if data[0:-2] == "IMG":
            print("Receiving Image")
            logimg()
            print("Image Received")
    if keyboard.is_pressed("q"): # Press the 'q' key on the keyboard to quit the program
        exit(0)

while True:
    loopfunc()
