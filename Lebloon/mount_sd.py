import board
import busio
import sdcardio
import storage

class SDCardHandler:
    def __init__(self, spi, cs_pin=board.D10):
        # Set up SPI and CS pin
        self.spi = spi
        self.cs = cs_pin
        self.sdcard = None
        self.mounted = False

        # Initialize and mount the SD card
        self._initialize_sd()


    def _initialize_sd(self):
        try:
            # Initialize SD card and mount it
            self.sdcard = sdcardio.SDCard(self.spi, self.cs)
            vfs = storage.VfsFat(self.sdcard)
            storage.mount(vfs, "/sd")
            print("SD card successfully mounted.")
            self.mounted = True
        except OSError as e:
            print("Failed to mount SD card:", e)
            self.mounted = False

    def write(self, filename, data):
        if not self.mounted:
            print("SD card is not mounted.")
            return
        try:
            with open(f"/sd/{filename}", "a") as file:  # Open in append mode
                file.write(data + "\n")
                #print(f"Data written to {filename}")
        except OSError as e:
            print(f"Failed to write to {filename}:", e)

    def read(self, filename):
        if not self.mounted:
            print("SD card is not mounted.")
            return
        try:
            with open(f"/sd/{filename}", "r") as file:  # Open in read mode
                content = file.read()
                #print(f"Data read from {filename}:")
                #print(content)
                return content
        except OSError as e:
            print(f"Failed to read from {filename}:", e)
            return None

    def file_exists(self, filename):
        """Check if a file exists on the SD card."""
        if not self.mounted:
            print("SD card is not mounted.")
            return False
        try:
            with open(f"/sd/{filename}", "r"):
                return True
        except OSError:
            return False

    def newFile(self):
        count = 0
        filename = 'log.txt'
        while self.file_exists(filename):
            count += 1
            filename = 'test_log' + str(count) + '.txt'
        return filename
    # Logsd:
    def logsd(self, data, filename):
        self.write(filename, str(data))


