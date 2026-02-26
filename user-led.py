# Lab 5 code for LED ON OFF through user input 
import serial
import time


#windows - make sure matches the com port in the Arduino IDE
ser = serial.Serial('/dev/cu.usbmodem2101', 9600, timeout=.1)

#mac - - make sure matches the com port in the Arduino IDE
#ser = serial.Serial('/dev/cu.usbmodem21401', 9600, timeout=.1)

def led_on_off():
   while True:
    user_input = input("\nEnter ON, OFF or QUIT: ").strip()
    # convert input to lowercase for easier comparison
    input_lower = user_input.lower()

    if "on" in input_lower:
        print("LED is switched ON")
        ser.write(b'H')
    elif "off" in input_lower:
        print("LED is switched OFF")
        ser.write(b'L')
    elif "quit" in input_lower:
        print("Quitting program...")
        break
    else:
        print("Invalid input. Please type ON, OFF, or QUIT.")
    #led_on_off() if you want to use reccursion 
    #elif ----- fill in rest of the code

time.sleep(2)
led_on_off()