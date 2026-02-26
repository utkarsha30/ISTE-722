# Lab 5 - LED ON and OFF
import serial
import time

#windows - make sure matches the com port in the Arduino IDE
ser = serial.Serial('/dev/cu.usbmodem2101', 9600, timeout=.1)

#mac - - make sure matches the com port in the Arduino IDE
#ser = serial.Serial('/dev/cu.usbmodem21401', 9600, timeout=.1)

for i in range(10):
        time.sleep(0.5)
        ser.write(b'H')   # send the pyte string 'H'
        time.sleep(0.5)   # wait 0.5 seconds
        ser.write(b'L')   # send the byte string 'L'