#Lab 5 - Read Serial Data
import serial

#windows - make sure matches the com port in the Arduino IDE
arduino = serial.Serial('/dev/cu.usbmodem2101', 115200, timeout=.1)

#mac - - make sure matches the com port in the Arduino IDE
#arduino = serial.Serial('/dev/cu.usbmodem21401', 115200, timeout=.1)

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print(data)