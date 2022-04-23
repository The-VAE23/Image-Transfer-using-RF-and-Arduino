# Required Libraries
from functions import *
import cv2 as cv
from matplotlib import pyplot as plt

#Load Image File into memory
img = cv.imread("D:/Data/sample.jpg",0)

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

#Perform Transmission and time the code
print("Sending image now. Starting timer")
t=time.perf_counter()
sendIMGdata(img,AR)
print("Image sent")
print("Time taken to send image: ",time.perf_counter()-t)
