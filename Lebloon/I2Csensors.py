import time
import board
import adafruit_bmp280
import adafruit_bno055
import adafruit_scd4x
import adafruit_gps

class BMP280:
    def __init__(self, i2c):
       self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
       self.bmp280.sea_level_pressure = 1013.25
       self.temp = 0
       self.pressure = 0
       self.alt = 0

    def sensor_read(self):
        try:
            self.temp = self.bmp280.temperature
            self.pressure = self.bmp280.pressure
            self.alt = self.bmp280.altitude
        except Exception as e:
            self.temp = 0
            self.pressure = 0
            self.alt = 0

class BNO055:
    def __init__(self, i2c):
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)
        self.last_val = 0xFFFF

    def temperature(self):
        global last_val  # pylint: disable=global-statement
        result = sensor.temperature
        if abs(result - last_val) == 128:
            result = sensor.temperature
            if abs(result - last_val) == 128:
                return 0b00111111 & result
        last_val = result
        return result

    def sensor_read(self):
        return "\n".join([
            "Temperature: {} degrees C".format(self.sensor.temperature),
            "Accelerometer (m/s^2): {}".format(self.sensor.acceleration),
            "Magnetometer (microteslas): {}".format(self.sensor.magnetic),
            "Gyroscope (rad/sec): {}".format(self.sensor.gyro),
            "Euler angle: {}".format(self.sensor.euler),
            "Quaternion: {}".format(self.sensor.quaternion),
            "Linear acceleration (m/s^2): {}".format(self.sensor.linear_acceleration),
            "Gravity (m/s^2): {}".format(self.sensor.gravity)
        ])


class SCD41:
    def __init__(self, i2c):
        self.scd4x = adafruit_scd4x.SCD4X(i2c)
        self.scd4x.start_periodic_measurement()
        self.co2 = 0
        self.temp = 0
        self.humidity = 0

    def sensor_read(self):
        if self.scd4x.data_ready:
            try:
                self.co2 = self.scd4x.CO2
                self.temp = self.scd4x.temperature
                self.humidity = self.scd4x.relative_humidity

            except Exception as e:
                self.temp = 0
                self.pressure = 0
                self.alt = 0
        else:
            self.temp = 0
            self.pressure = 0
            self.alt = 0

class GPS:
    def __init__(self, i2c):
        self.gps = adafruit_gps.GPS_GtopI2C(i2c)
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,1000")

        self.lat = 0
        self.long = 0

    def sensor_read(self):
        self.gps.update()

        # Check if there is a fix and the data is valid
        if not self.gps.has_fix:
            #print("Waiting for fix...")
            self.lat = 0
            self.long = 0
            self.alt = 0
            self.speed_kmh = 0
            self.satellites = 0
            return None

        # Read latitude, longitude, altitude, speed, and number of satellites
        latitude = self.gps.latitude
        longitude = self.gps.longitude
        altitude = self.gps.altitude_m  # Altitude in meters
        speed = self.gps.speed_knots    # Speed in knots
        satellites = self.gps.satellites  # Number of satellites in view

        # Convert speed to km/h
        speed_kmh = speed * 1.852 if speed is not None else 0

        # Store values if they are valid
        if latitude is not None and longitude is not None:
            self.lat = latitude
            self.long = longitude
            self.alt = altitude if altitude is not None else 0
            self.speed_kmh = speed_kmh
            self.satellites = satellites if satellites is not None else 0
        else:
            self.lat = 0
            self.long = 0
            self.alt = 0
            self.speed_kmh = 0
            self.satellites = 0
