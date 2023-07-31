from machine import ADC, Pin
import time

sensor = ADC(Pin(26, Pin.IN))
min_moisture = 60000
max_moisture = 65535

while True:
    reading = sensor.read_u16()
    voltage = reading * 3.3 / 65535
    moisture = (reading - min_moisture)*100/(max_moisture - min_moisture)
    print("moisture: %.2f" % moisture + "% (adc: " + str(reading) + ", voltage: " + str(voltage) + ")")
    time.sleep(0.5)
