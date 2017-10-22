import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *

voltageArray=[]
ser = serial.Serial('COM1', 9600)
plt.ion()
cnt=0

def makeFig():
    plt.ylim(0, 1024)
    plt.title('Potential Difference v. Time')
    plt.grid(True)
    plt.ylabel('Potential Difference')
    plt.plot(voltageArray, 'ro-')

while True:
    while (ser.inWaiting()==0):
        pass
    voltage = float(ser.readline())
    voltageArray.append(voltage)
    drawnow(makeFig)
    plt.pause(0.000001)
    cnt=cnt+1
    if(cnt>50):
        voltageArray.pop(0)
