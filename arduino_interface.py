import time
import serial

arduino = serial.Serial(port='COM8', baudrate=115200, timeout=.1)
ser = serial.Serial(
    port='COM6',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=False,
    dsrdtr=False,
    xonxoff=False,
    timeout=0.5
)
ser.rts = False
on = False
while True:
    data = arduino.read()
    if data == b"0":
        #print("on")
        ser.rts = True

    else:
        ser.rts = False




