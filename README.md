# LeBloon
Stanford Student Space Initiative High Altitude Balloon Payload Recources / Guide  

## Intro: 

The contents of this repository are for a balloon payload designed for latex balloon launches. The goal of these launches are to obtain footage, weather and other data (humitity, pressure, gps coords, temperature, ect.), to make assembly simpler, and to make recovery more feasable.  

Each section is divided into a Payload and Ground Station group, with each group contating the relevant information about each group of electronics. The payload group of electronics are the electrnoics excluding dji/gopro cameras and the featherweight GPS electronics that are found of the balloon payload. The Ground Station group are the electronics featured only on the ground station board which is a handheld device used for tracking and obatining telemetry from the payload at reletivly small distances (~1000 m w/out obstructions)

## Components: 

### Payload: 
#### microcontroller: 
Adafruit Feather nRF52840 Sense | https://www.adafruit.com/product/4516?gad_source=1&gad_campaignid=21079227318&gbraid=0AAAAADx9JvSbOUzcF4ef_L69nVPg6Z2u9&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJTMS-gGHyZneq7OiJb5g3dyKN5okFDrAj3ocPelJ5noS5pyaqTsRUBoC9ukQAvD_BwE 

#### SD Card reader/ writer: 

#### Lora Radio: 

#### 

#### 

## Ground Station: 
#### microcontroller:  
Adafruit Feather M4 Express - Featuring ATSAMD51 - ATSAMD51 Cortex M4 | https://www.adafruit.com/product/3857?gad_source=1&gad_campaignid=21079267614&gbraid=0AAAAADx9JvRParWJ6U18OcWQZk40H3eIZ&gclid=CjwKCAjwvO7CBhAqEiwA9q2YJelPlcSGU9BHIFvF0gTP1EcTx982lZVC1w_qEUdXl5dNRQfYslb-GRoCdJ4QAvD_BwE

## Intructions 
In order to assemble the payload please follow these instructions: 

### Wiring:  

### Code:  
In order to install the proper software follow the steps below beginning with the payload microcontoller. This tutorial assumes the use of a Adafruit Feather nRF52840 Sense using CircuitPython, closely following the guide: https://learn.adafruit.com/adafruit-feather-sense/circuitpython-on-feather-sense.  (useful if you want to use arduino instead: https://learn.adafruit.com/adafruit-feather-sense/arduino-ble-examples)   

For the ground station however it assumes the use of a adafruit 

This is intended to be a short guide to help one get the devices up and running to understand the code written and how these steps work closer please refer to the mentioned adafruit tutorials and read the comments and code in the repository :) (excerise for the reader)

#### Payload
Step 1: Install udf files    

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

