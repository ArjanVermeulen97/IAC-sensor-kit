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

dev = True              # Development mode
usbPort = "editMe"      # Your USB port, obtain using port_scan()

try:
    if not dev:
        ser = serial.Serial(usbPort, 9600)
    running = True
    print("Serial initialized succesfully!")
except:
    print("Issue with serial! Aborting...")


if dev:
    currentTime = time.time()
    while running:
        # Delay 1 second
        while currentTime + 1 > time.time():
            pass
        currentTime = time.time()
        line = development_data()[:-2].decode('utf-8')
        print(line)
    
        ####################
        ###YOUR CODE HERE###
        ####################
else:
    while running:
        line = ser.readline()[:-2].decode('utf-8')
        print(line)
        
        ####################
        ###YOUR CODE HERE###
        ####################