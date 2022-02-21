# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:36:29 2022

@author: Arjan
"""

import usb
import usb.util
import os
os.environ["BLINKA_FT232H"] = "1"
import board2
import adafruit_vl53l1x
import time

i2c = board2.I2C()
vl53 = adafruit_vl53l1x.VL53L1X(i2c)

print("VL53L1X Simple Test.")
print("--------------------")
model_id, module_type, mask_rev = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Mask Revision: 0x{:0X}".format(mask_rev))
print("Distance Mode: ", end="")
if vl53.distance_mode == 1:
    print("SHORT")
elif vl53.distance_mode == 2:
    print("LONG")
else:
    print("UNKNOWN")
print("Timing Budget: {}".format(vl53.timing_budget))
print("--------------------")

vl53.start_ranging()

while True:
    if vl53.data_ready:
        print("Distance: {} cm".format(vl53.distance))
        vl53.clear_interrupt()
        time.sleep(1.0)