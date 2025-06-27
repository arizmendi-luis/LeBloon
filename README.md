# LeBloon
Stanford Student Space Initiative High Altitude Balloon Payload Recources / Guide  

## Intro: 

The contents of this repository are for a balloon payload designed for latex balloon launches. The goal of these launches are to obtain footage, weather and other data (humitity, pressure, gps coords, temperature, ect.), to make assembly simpler, and to make recovery more feasable.  

Each section is divided into a Payload and Ground Station group, with each group contating the relevant information about each group of electronics. The payload group of electronics are the electrnoics excluding dji/gopro cameras and the featherweight GPS electronics that are found of the balloon payload. The Ground Station group are the electronics featured only on the ground station board which is a handheld device used for tracking and obatining telemetry from the payload at reletivly small distances (~1000 m w/out obstructions)

## Components: 

### Payload: 
#### microcontroller: 
Adafruit Feather nRF52840 Sense | https://www.adafruit.com/product/4516?gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvSbOUzcF4ef_L69nVPg6Z2u9&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJTMS-gGHyZneq7OiJb5g3dyKN5okFDrAj3ocPelJ5noS5pyaqTsRUBoC9ukQAvD_BwE  

battery: Lithium Ion Polymer Battery - 3.7v 1200mAh | https://www.adafruit.com/product/258, but most 3.7v lipobatteries work 

#### SD Card reader/ writer (via SPI):  
Adafruit Micro SD SPI | https://www.adafruit.com/product/4682  

Note: best to use 16GB or lower, safest is the use of an 8GB SD card, however 32GB can work 
- Make sure to use correct OS (FAT16 or FAT32)

#### Lora Radio (SPI): 
Adafruit RFM95W LoRa Radio Transceiver Breakout - 868 or 915 MHz - RadioFruit | https://www.adafruit.com/product/3072  

(solder a solid core wire ~3in (TODO: virfy this length and gauge) as antenna)

#### Rockblock (UART): 
RockBLOCK 9603 with USB Cable - Iridium Satellite Modem Bundle | https://www.adafruit.com/product/4521  

antenna: GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA | https://www.adafruit.com/product/960 
PCB/solderable 10 pin molex connector:  CONN HEADER SMD 10POS 1.25MM | https://www.digikey.com/en/products/detail/molex/0533981071/699074?s=N4IgTCBcDaIOoFkDsA2AjAFgMIBUC0AcgCIgC6AvkA
10 pin cable: 1.25mm Pitch 10-pin Cable 20cm long 1:1 Cable - Molex PicoBlade Compatible | https://www.adafruit.com/product/4930   

4x lipo batteries: https://www.amazon.com/Energizer-Ultimate-Lithium-Batteries-Pack/dp/B0023T8OUY/ref=sr_1_6?crid=1RYVEUVL0USYI&dib=eyJ2IjoiMSJ9._HeDeh0wcziJr4SSHjyDo9SGiTTNP6PYenHgorRVyVbPS6BvJ5eI_G95ZVrosiDqiBwUY_gQ5Yv2q-zDD6MszF6a5VH1IetSNLezYu1VxZlycmU6_FvMupd_LOu_hMNECZ7CDxLFigNPs-GM38zSlOn-3wxHg8M7q9iLqmYOjqiBHyvcjqOTvCrgLvHZJOGZqhWusFtRurtDfsFa9iH55yBpln8Bbyq0rni7ZV9jNhJC4ELQ_-3NewgewQ9mzzlH-2tFetWurT5v8tlbXFSNa6Gm_9HejEavXOiECUDc984.7GPuGnXEZTJVAp7zyglEl93Ez05XwvMmGQLMFUa6E0A&dib_tag=se&keywords=energizer%2Blipo%2B1.5v&qid=1750902239&sprefix=enegizer%2Blipo%2B1.5v%2Caps%2C158&sr=8-6&th=1   

Buck converter: DROK DC 12V to 5V Buck Converter, 10pcs Mini Voltage Regulator Board DC 4.5-20V 12V 9V Step Down to 1-16V 5V Reducer 3A Fixed Adjustable Volt Output Transformer Power Supply Stabilizer Module | https://www.amazon.com/dp/B08Q3TKJH5?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1 

* To purchase credits from ground control

#### IMU (I2C): 
Adafruit 9-DOF Absolute Orientation IMU Fusion Breakout - BNO055 - STEMMA QT / Qwiic | https://www.adafruit.com/product/4646  

#### GPS (I2C): 
Adafruit Mini GPS PA1010D - UART and I2C - STEMMA QT | https://www.adafruit.com/product/4415 

#### CO2 + Humidity sensor (I2C): 
Adafruit SCD-41 - True CO2 Temperature and Humidity Sensor - STEMMA QT / Qwiic | https://www.adafruit.com/product/5190  

#### Altimiter (I2C): 
Adafruit BMP280 I2C or SPI Barometric Pressure & Altitude Sensor - STEMMA QT | https://www.adafruit.com/product/2651

#### I2C wires 
Long I2C cable: STEMMA QT / Qwiic JST SH 4-Pin Cable - 400mm long | https://www.adafruit.com/product/5385 
short I2C cable: STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long | https://www.adafruit.com/product/4399 
Breadboard cable: STEMMA QT / Qwiic JST SH 4-pin to Premium Male Headers Cable - 150mm Long | https://www.adafruit.com/product/4209

## Ground Station: 
#### microcontroller:  
Adafruit Feather M4 Express - Featuring ATSAMD51 - ATSAMD51 Cortex M4 | https://www.adafruit.com/product/3857?gad_source=1&gad_campaignid=21079267614&gbraid=0AAAAADx9JvRParWJ6U18OcWQZk40H3eIZ&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJelPlcSGU9BHIFvF0gTP1EcTx982lZVC1w_qEUdXl5dNRQfYslb-GRoCdJ4QAvD_BwE  

#### SD Card reader/ writer (via SPI):  
Adafruit Micro SD SPI | https://www.adafruit.com/product/4682  

Note: best to use 16GB or lower, safest is the use of an 8GB SD card, however 32GB can work 
- Make sure to use correct OS (FAT16 or FAT32)

#### Lora Radio: 
Adafruit RFM95W LoRa Radio Transceiver Breakout - 868 or 915 MHz - RadioFruit | https://www.adafruit.com/product/3072  

ordered with (and attached): Edge-Launch SMA Connector for 1.6mm / 0.062" Thick PCBs | https://www.adafruit.com/product/1865, 2.4GHz Dipole Swivel Antenna with RP-SMA - 2dBi| https://www.adafruit.com/product/944gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvSbOUzcF4ef_L69nVPg6Z2u9&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJR_6mnKnE-62oneQ1XhGRXBMDKE88t1kSeRQSbKNTflh6k_tuNEs4xoCyAkQAvD_BwE 

#### Display: 
Adafruit FeatherWing OLED - 128x64 OLED Add-on For Feather - STEMMA QT / Qwiic | https://www.adafruit.com/product/4650 

Mount on top of feather with: 
Stacking Headers for Feather - 12-pin and 16-pin female headers | https://www.adafruit.com/product/2830

## Intructions 
In order to assemble the payload please follow these instructions: 

### Wiring:  

### Code:  
In order to install the proper software follow the steps below beginning with the payload microcontoller. This tutorial assumes the use of a Adafruit Feather nRF52840 Sense using CircuitPython, closely following the guide: https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense.  (useful if you want to use arduino instead: https://learn.adafruit.com/adafruit-feather-sense/arduino-ble-examples)   

For the ground station however it assumes the use of a adafruit 

This is intended to be a short guide to help one get the devices up and running to understand the code written and how these steps work closer please refer to the mentioned adafruit tutorials and read the comments and code in the repository :) (excerise for the reader)

#### Payload
Step 1: Install uf2 files    

a. From uf2 files folder select the: adafruit-circuitpython-feather_bluefruit_sense-en_US-9.2.7 (2).uf2 file
b. Plug in the microcontroller to you laptop via USB
c. Press the Reset button on the microtroller twice (double click) and wait for FTHRSNBOOT to appear in your computer's file explorer
d. drag the uf2 file into this folder 

Tutorial: https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense 
File can be found: https://circuitpython.org/board/feather_bluefruit_sense/  

Step 2: Install code  
a. Replace and add the files in Lebloon into the root dir of the microcntroller. 

Note: this step is kind of done for you but if you wanted to add devices/ adafruit libraries in the future you would navigate to the lib folder and add them there a good place to find libraries is from here: https://circuitpython.org/libraries, especially from the community bundle (it is not a great idea to add unused libraries into your micronctrollers lib folder, its just using up storage!)  

Futhermore if you want to understand how the code runs: 
1. Your microntroller assumes that the code.py file is the main file, code will run from here on start up
2. code.py will call libraries and other python files which have defined functions. Most of the code is ran in the while loop.
3. Otherwise functions like any other python file.

#### Ground Station 
(This section is very similar to the Payload except it will be using different files)   

a. From uf2 files folder select the:  adafruit-circuitpython-feather_m4_express-en_US-9.2.7 (4).uf2 file
b. Plug in the microcontroller to you laptop via USB
c. Press the Reset button on the microtroller twice (double click) and wait for FTHRSNBOOT to appear in your computer's file explorer
d. drag the uf2 file into this folder 

Tutorial: https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython
File can be found: https://circuitpython.org/board/feather_m4_express/  

a. Replace and add the files in LeGround Station into the root dir of the microcntroller.  

#### Plotting: 

1. Place the logged data from the sd cards into the data folder. 
2. In the plot.py code look for the vraiable FILENAME: change that filename path to the one you want to analyze 
3. run plot.py 

The sd cards will create a new log at power up, usally differentiated with an increasing number at the end. The larger the number the more recent the log is.  

Please view the data folder README for slightly more info


