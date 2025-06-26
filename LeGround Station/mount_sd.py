import board
import busio
import sdcardio
import storage

spi = board.SPI()
cs = board.D10

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

storage.mount(vfs, "/sd")



