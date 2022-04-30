# Required Libraries
import serial
import time
import numpy as np
from math import *

def printSerial(Aobj: serial):
    """Function to read and print serial buffer from Arduino object"""
    x=Aobj.inWaiting()
    while x>0:
        print(Aobj.readline().decode('utf-8'))
        x=Aobj.inWaiting()


def writeSerial(Aobj: serial,CMD):
    """Function to write serial data to Arduino object."""
    try:
        Aobj.write(bytes(str(CMD),'utf-8'))
    except:
        print("Serial Write operation failed for Arduino"+str(Aobj))

def readSerial(Aobj: serial):
    """Function to read data from Arduino object"""
    data = Aobj.readline()
    return data

def sendIMGdata(IMG: np.array,AR: serial):
    """Function used to send img data over RF"""
    writeSerial(AR,2)
    IMG = IMG.reshape((1,np.size(IMG)))
    i=0
    data=0
    while i < IMG.size:
        x = AR.inWaiting()
        if x>0:
            data = readSerial(AR).decode('utf-8')
        else:
            data = "0"
        if int(data) == 1:
            if IMG.size - i > 7:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])+','+str(IMG[0,i+3])+','+str(IMG[0,i+4])+','+str(IMG[0,i+5])+','+str(IMG[0,i+6])+','+str(IMG[0,i+7])
                writeSerial(AR,string)
            elif IMG.size - i == 7:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])+','+str(IMG[0,i+3])+','+str(IMG[0,i+4])+','+str(IMG[0,i+5])+','+str(IMG[0,i+6])
                writeSerial(AR,string)
            elif IMG.size - i == 6:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])+','+str(IMG[0,i+3])+','+str(IMG[0,i+4])+','+str(IMG[0,i+5])
                writeSerial(AR,string)
            elif IMG.size - i == 5:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])+','+str(IMG[0,i+3])+','+str(IMG[0,i+4])
                writeSerial(AR,string)
            elif IMG.size - i == 4:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])+','+str(IMG[0,i+3])
                writeSerial(AR,string)
            elif IMG.size - i == 3:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])+','+str(IMG[0,i+2])
                writeSerial(AR,string)
            elif IMG.size - i == 2:
                string = str(IMG[0,i])+','+str(IMG[0,i+1])
                writeSerial(AR,string)
            elif IMG.size - i == 1:
                string = str(IMG[0,i])
                writeSerial(AR,string)
            i+=8
            i=i if i < IMG.size else IMG.size
            print(str(i)+'/'+str(IMG.size))
    time.sleep(1)
    writeSerial(AR,"e")
