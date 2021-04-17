from bme680 import BME680

bme = BME680()

print(bme.data.temperature)
print(bme.data.pressure)
print(bme.data.humidity)
print(bme.data.gas_resistance)
