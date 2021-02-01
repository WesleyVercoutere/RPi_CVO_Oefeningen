import time
import RPi.GPIO as GPIO

red = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)

p = GPIO.PWM(red, 50)  # channel=14  frequency=50Hz
p.start(0)


while True:
    for dc in range(0, 101):
        p.ChangeDutyCycle(dc)
        time.sleep(0.02)
    for dc in range(100, -1, -1):
        p.ChangeDutyCycle(dc)
        time.sleep(0.02)
    time.sleep(2)


p.stop()
GPIO.cleanup()
