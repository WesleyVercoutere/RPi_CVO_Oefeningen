import RPi.GPIO as GPIO
import time

led = 12
cycleTime = 2 # seconden
frequenty = 100

update = cycleTime / 100
updateValue = 1

dc = 0
sleep = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

p = GPIO.PWM(led, frequenty)
p.start(dc)

startTime = time.time()

def updateDutyCycle():
    global dc
    global updateValue
    
    # Update duty cycle
    dc += updateValue
    
    # Add or Subtract
    if dc >= 100:
        updateValue = -1
    if dc <= 0:
        updateValue = 1


while True:
    currentTime = time.time()

    if (currentTime >= startTime + update) and not sleep:
        startTime = time.time()
        updateDutyCycle()
        p.ChangeDutyCycle(dc)

    if dc == 0:
        sleep = True

    if sleep and (currentTime >= startTime + cycleTime):
        sleep = False
        

p.stop()
GPIO.cleanup()
