
import sys
import Adafruit_DHT
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 22)

    print(humidity, temperature)
    time.sleep(4)