# import necessary libraries
import time
import board
import busio
import digitalio
import neopixel
import adafruit_rfm9x
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_displayio_sh1107 import SH1107
from i2cdisplaybus import I2CDisplayBus

import sdcardio
import storage
import adafruit_sdcard

# ==================== DisplayIO release fix ====================
displayio.release_displays()

# ==================== NeoPixel setup ====================
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

def flash_blue(duration=0.5):
    pixel[0] = (0, 0, 50)
    time.sleep(duration)
    pixel[0] = (0, 0, 0)

flash_blue(0.5)

# ==================== Shared I2C setup ====================
i2c = board.I2C()

# ==================== OLED Display (SH1107) ====================
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
WIDTH = 128
HEIGHT = 64
display = SH1107(display_bus, width=WIDTH, height=HEIGHT)

splash = displayio.Group()
display.root_group = splash

# ==================== SDCard Module setup ====================
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = board.D10

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# ==================== LoRa RFM9x setup ====================
RADIO_FREQ_MHZ = 915.0 # Adjust to your region's frequency/ make sure its not thes same as another device pair
CS = digitalio.DigitalInOut(board.D5)
RESET = digitalio.DigitalInOut(board.D6)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

print("active")

# ==================== Main loop ====================
last_flash = time.monotonic() 

splash = displayio.Group()
display.root_group = splash
splash.append(label.Label(terminalio.FONT, text="Active", x=0, y=5))

while True:
    if time.monotonic() - last_flash >= 60:
        flash_blue(0.2)
        last_flash = time.monotonic()

    packet = rfm9x.receive(timeout=0.5)

    if packet is not None:
        packet_text = str(packet, "ascii")
        rssi = rfm9x.last_rssi

        # === Smart SBDIX parsing and cleanup ===
        if "AT+SBDIX" in packet_text:
            # Remove newlines and excess whitespace
            cleaned = packet_text.replace("\r", "").replace("\n", "").replace(" ", "")
            if "+SBDIX:" in cleaned:
                sbdix_data = cleaned.split("+SBDIX:")[1]
                sbdix_fields = sbdix_data.split(",")
                sbdix_numbers = [f for f in sbdix_fields if f.strip().isdigit()]
                clean_result = ",".join(sbdix_numbers[:6])
                # Replace everything from AT+SBDIX onward with clean_result
                packet_text = packet_text.split("AT+SBDIX")[0] + "    " + clean_result

        # === Now do normal parsing based on 4+ spaces ===
        parts = []
        space_count = 0
        word = ""
        in_spaces = 0

        for c in packet_text:
            if c == " ":
                space_count += 1
                if space_count >= 4:
                    in_spaces = 1
            if c != " ":
                in_spaces = 0
            if space_count >= 4:
                if in_spaces == 0:
                    in_spaces = 0
                    parts.append(word)
                    word = ""
                    space_count = 0
            if in_spaces == 0:
                word += c
        parts.append(word)

        print(parts)
        print("Received (ASCII):", packet_text)
        print("RSSI:", rssi)

        # === OLED update ===
        splash = displayio.Group()
        display.root_group = splash

        splash.append(label.Label(terminalio.FONT, text="Packet:", x=0, y=5))
        splash.append(label.Label(terminalio.FONT, text=f"RSSI: {rssi} dB", x=0, y=60))

        for i in range(min(len(parts), 6)):
            splash.append(label.Label(terminalio.FONT, text=parts[i], x=0, y=(20 + (i * 10))))

        # === SD card logging ===
        try:
            with open("/sd/data.txt", "a") as fp:
                fp.write(f"RSSI: {rssi} dB  {parts}\n")
        except Exception as e:
            print("Failed to write to SD card:", e)

        time.sleep(10)
