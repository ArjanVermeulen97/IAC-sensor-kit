/*
  Use the Qwiic Scale to read load cells and scales
  By: Nathan Seidle @ SparkFun Electronics
  Date: March 3rd, 2019
  License: This code is public domain but you buy me a beer if you use this 
  and we meet someday (Beerware license).

  The Qwiic Scale is an I2C device that converts analog signals to a 24-bit
  digital signal. This makes it possible to create your own digital scale
  either by hacking an off-the-shelf bathroom scale or by creating your
  own scale using a load cell.

  This example merely outputs the raw data from a load cell. For example, the
  output may be 25776 and change to 43122 when a cup of tea is set on the scale.
  These values are unitless - they are not grams or ounces. Instead, it is a
  linear relationship that must be calculated. Remeber y = mx + b?
  If 25776 is the 'zero' or tare state, and 43122 when I put 15.2oz of tea on the
  scale, then what is a reading of 57683 in oz?

  (43122 - 25776) = 17346/15.2 = 1141.2 per oz
  (57683 - 25776) = 31907/1141.2 = 27.96oz is on the scale
  
  SparkFun labored with love to create this code. Feel like supporting open
  source? Buy a board from SparkFun!
  https://www.sparkfun.com/products/15242

  Hardware Connections:
  Plug a Qwiic cable into the Qwiic Scale and a RedBoard Qwiic
  If you don't have a platform with a Qwiic connection use the SparkFun Qwiic Breadboard Jumper (https://www.sparkfun.com/products/14425)
  Open the serial monitor at 9600 baud to see the output
*/

#include <Wire.h>

#include "SparkFun_Qwiic_Scale_NAU7802_Arduino_Library.h" // Click here to get the library: http://librarymanager/All#SparkFun_NAU7802
#include "SparkFun_VL53L1X.h" //Click here to get the library: http://librarymanager/All#SparkFun_VL53L1X

NAU7802 Scale; //Create instance of the NAU7802 class
SFEVL53L1X distanceSensor;
int startPin = 15;
unsigned int measurements = 0;
unsigned long lastOutput = 0;
long totalScale = 0;
long totalToF = 0;
unsigned long runTime;


void setup()
{
  Serial.begin(9600);
  Serial.println("IAC Sensor kit, v0.2");
  
  delay(10);
  Wire.begin();
  delay(10);
  
  Serial.println("Time of Flight...");
  if (distanceSensor.begin() != 0) //Begin returns 0 on a good init
  {
    Serial.println(" failed to begin. Please check wiring. Freezing...");
    while (1)
      ;
  } else {
    Serial.println(" success!");
  }

Serial.print("Load Cell...");
  if (Scale.begin() == false)
  {  
    Serial.println(" not detected. Please check wiring. Freezing...");
    while (1);
  } else {
    Serial.println(" success!");
  }
  
  Serial.println("Sensors initiated!");
}

void loop()
{
  runTime = millis();
  if (runTime - lastOutput > 100)
  {
    distanceSensor.startRanging();
    totalToF = totalToF + distanceSensor.getDistance();
    distanceSensor.clearInterrupt();
    distanceSensor.stopRanging();

    delay(1);
    totalScale = totalScale + Scale.getReading();
    
    measurements++;
    lastOutput = runTime;
    if (measurements == 10) {
      Serial.print("load_cell: ");
      Serial.print(totalScale);
      Serial.print(" time_of_flight: ");
      Serial.println(totalToF / 25.4);
      measurements = 0;
      totalScale = 0;
      totalToF = 0;
    }
  }
}
