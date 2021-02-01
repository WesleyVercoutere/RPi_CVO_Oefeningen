import RPi.GPIO as GPIO     # https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import time                 # https://docs.python.org/2/library/time.html?highlight=time%20time#module-time

# Pin variables
red = 17
orange = 18
green = 20

colors = [red, orange, green]

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in colors:
    GPIO.setup(i, GPIO.OUT)

# Loop
while True:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(14, GPIO.LOW)
    time.sleep(1)
