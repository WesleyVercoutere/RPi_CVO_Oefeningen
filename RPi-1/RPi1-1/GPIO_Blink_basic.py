import RPi.GPIO as GPIO     # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import time                 # https://docs.python.org/2/library/time.html?highlight=time%20time#module-time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while True:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(14, GPIO.LOW)
    time.sleep(1)
