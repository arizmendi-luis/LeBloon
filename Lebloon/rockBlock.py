import time
import board
import busio

class rockBlock:
    def __init__(self):
        self.count = 600
        # Initialize UART
        uart = busio.UART(board.TX, board.RX, baudrate=19200, timeout=1)
        #uart = board.UART()
        uart.baudrate = 19200
        self.uart = uart
        self.lastCode = None

    def send_at_command(self, command, wait_time=2):
        """
        Send an AT command to the RockBLOCK and wait for a response.

        :param command: The AT command to send (string).
        :param wait_time: Time to wait for a response in seconds.
        :return: Response from the RockBLOCK.
        """
        print(f"Sending: {command}")
        self.uart.write((command + '\r').encode('utf-8'))  # Send command with carriage return
        time.sleep(wait_time)  # Wait for response
        response = self.uart.read(256)  # Read up to 256 bytes from UART
        if response:
            return response.decode('utf-8', 'ignore')
        else:
            return None
    def attempt_send(self, message):
        # Basic AT command to verify communication
        response = self.send_at_command("AT")
        print(f"Response: {response}")

        # Check signal quality
        response = self.send_at_command("AT+CSQ")
        print(f"Signal Quality: {response}")

        # Send a short burst data message
        self.send_at_command("AT+SBDD0")  # Clear the message buffer
        response = self.send_at_command(f"AT+SBDWT={message}")
        print(f"Write Message Response: {response}")

        # Initiate a satellite session
        response = self.send_at_command("AT+SBDIX", wait_time=30)  # Satellite session may take longer
        print(f"Satellite Transfer Response: {response}")
        self.lastCode = response
        print(f'bruh {self.lastCode}')

        # Done
        print("Done.")
