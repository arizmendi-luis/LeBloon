import time
import board
import digitalio
import busio


import neopixel

from rockBlock import rockBlock
from I2Csensors import BMP280,SCD41, GPS, BNO055
from mount_sd import SDCardHandler
import adafruit_rfm9x



print('hello')
#==================Debug lights ====================
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
def lightGo(color, wait=0.25):
    if color == 'green':
        pixel[0] = (0, 10, 0)  # Green
    if color == 'purple':
        pixel[0] = (10, 0, 10)
    if color == 'orange':
        pixel[0] = (10, 10, 0)
    if color == 'blue':
        pixel[0] = (0, 0, 10)
    time.sleep(wait)  # Wait half a second
    pixel[0] = (0, 0, 0)  # Off

def HoldOn():
    pixel[0] = (5, 1, 5)  # Off

def HoldOff():
    pixel[0] = (0, 0, 0)  # Off

#================ Setup boards =======================
# ------ SPI chain ---
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# ==================== LoRa RFM9x setup ====================
RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.D5)
RESET = digitalio.DigitalInOut(board.D6)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23
# ----- SD card ------
sdcard = SDCardHandler(spi)
lightGo('orange', 0.5)
filename = sdcard.newFile()
print(filename)
# ----- I2C Chain------
i2c = board.I2C()
bmp280 = BMP280(i2c)
BNO = BNO055(i2c)
scd = SCD41(i2c)
gps = GPS(i2c)
# ----- RockBlock ------
rock = rockBlock()

# ============== Time blocks ========================
SD_interval = 4
Rock_interval = 30
last_SD_card_time = time.monotonic()
last_Rock_time = time.monotonic()
timeout_dur = 5

# ============= Miscellanous =====================
data = 'no data recorded yet'

last_rock_code = 'NA'

# What digit place to round to
acc = 2

# ============== Loop commands ===================
lightGo('orange')
while True:
    curr_time = time.monotonic() # Update curr time
    # Fill in SD card @ every ____ time
    if curr_time - last_SD_card_time >= SD_interval:
        bmp280.sensor_read()
        scd_data = scd.sensor_read()
        gps.sensor_read()
        bno_data = BNO.sensor_read()
        # bmp280_temp, bmp280_pressure, bmp280_alt, scd_co2, scd_temp, scd_humidity, gps_lat, gps_long, gps_alt, curr_time
        data = (f"{round(bmp280.temp, acc)} {round(bmp280.pressure, acc)} {round(bmp280.alt, acc)}\
                {round(scd.co2, acc)} {round(scd.temp, acc)} {round(scd.humidity, acc)}\
                {gps.lat} {gps.long}, {gps.alt }, {curr_time}")

        print(data)
        sdcard.logsd(data, filename)
        time.sleep(0.05)
        sdcard.logsd(bno_data, filename)
        time.sleep(0.05)
        lightGo('green')
        if last_rock_code:
            rfm9x.send(bytes(data + ' ' + last_rock_code, "utf-8"))
        last_SD_card_time = time.monotonic()
    # Attempt to send via rockblock here
    if curr_time - last_Rock_time >= Rock_interval:
        HoldOn()
        try:
            rock.attempt_send(data)
            HoldOff()
            last_rock_code = str(rock.lastCode)
            lightGo('blue', 1)
        except Exception as e:
            if rock.lastCode is None:
                last_rock_code = 'FA'
            else:
                last_rock_code = str(rock.lastCode)
            print('send message failed')
        HoldOff()
        last_Rock_time = time.monotonic()






