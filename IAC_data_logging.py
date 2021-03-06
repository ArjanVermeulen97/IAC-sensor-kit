# -*- coding: utf-8 -*-
"""
This program is used to load the data from the USB serial.
 Whenever the serial port receives data, it will be placed in
 the "line" variable. From here, it needs to be parsed and saved.
 
You can enable a "development" mode which will feed fake data 
 by setting dev = True
"""

import serial
import time
from IAC_helper import port_scan, development_data

### SETTINGS ###
dev = True              # Development mode
usbPort = "editMe"      # Your USB port, obtain using port_scan()

# Print information about USB devices
print("Connected USB Ports:")
port_scan()

# Attempt to initialize USB connection, if this fails, raise an error and abort.
try:
    if not dev:
        ser = serial.Serial(usbPort, 9600)
    running = True
    print("Serial initialized succesfully!")
except:
    running = False
    print("Issue with serial! Aborting...")
    print("Try reconnecting the USB cable")
print("")
print("Data from serial connection: ")


# Main loop
if dev:
    currentTime = time.time()
    while running:
        # Delay 1 second
        while currentTime + 1 > time.time():
            pass
        currentTime = time.time()
        # Read line from USB
        line = development_data()[:-2].decode('utf-8')
        print(line)
    
        ####################
        ###YOUR CODE HERE###
        ####################
else:
    while running:
        # Read line from USB
        line = ser.readline()[:-2].decode('utf-8')
        print(line)
        
        ####################
        ###YOUR CODE HERE###
        ####################
