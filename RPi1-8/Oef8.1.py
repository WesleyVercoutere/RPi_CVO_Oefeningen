import RPi.GPIO as GPIO
import time

led = 14
cyclus = 2 # seconden
update = cyclus / 100
dc = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

p = GPIO.PWM(led, 50)
p.start(dc)

startTime = time.time()

add = True

def updateDutyCycle():
    global add
    global dc
    
    # Update duty cycle
    if add:
        dc += update
    else:
        dc -= update

    # Add or Subtract
    if dc >= 100:
        add = False
    if dc <= 0:
        add = True


while True:
    currentTime = time.time()

    if currentTime >= startTime + update:
        startTime = time.time()

        updateDutyCycle()

        p.ChangeDutyCycle(dc)

p.stop()
GPIO.cleanup()
