#!/usr/bin/python3

from bme680 import BME680

bme = BME680()

try:
    while True:
        if bme.get_sensor_data():
            output = f"{bme.data.temperature:.2f} C,{bme.data.pressure:.2f} hPa,{bme.data.humidity:.3f} %RH"

except KeyboardInterrupt:
    pass
