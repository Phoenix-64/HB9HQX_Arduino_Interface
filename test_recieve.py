import time
import serial

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts=False,
    dsrdtr=False,
    xonxoff=False,
    timeout=0.5
)


while True:
    ser.dtr = True
    print("True")
    time.sleep(1)
    ser.dtr = False
    print("False")
    time.sleep(1)

while True:
    ser.rts = True
    print("True")
    time.sleep(2)
    ser.rts = False
    print("False")
    time.sleep(2)

# for dots set DTR true for dash set rts true

