# https://ph0en1x.net/86-raspberry-pi-znakomstvo-s-gpio-perekluchatel-i-svetodiod.html

import time
import RPi.GPIO as GPIO

timeout = 100
LED = 7

GPIO.cleanup()
GPIO.setup(LED, GPIO.OUT)
try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(timeout)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(timeout)
except KeyboardInterrupt:
    GPIO.cleanup()