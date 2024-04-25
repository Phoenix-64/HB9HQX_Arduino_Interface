import time
import serial
import numpy as np

arduino = serial.Serial(port='COM8', baudrate=115200, timeout=.1)
recieved = []

for i in range(0, 100000):
    data = arduino.read()
    recieved.append(data)
    print(data)

x = np.where(np.roll(recieved,1)!=recieved)[0]
sep = np.diff(x)
print(sep)

