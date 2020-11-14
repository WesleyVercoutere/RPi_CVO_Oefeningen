from tkinter import Tk

try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)


root = Tk()
root.title('Les 7 - Oef 1')
root.geometry('800x400')

# GPIO general
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Inputs
pinPushBtn = 25
pinRotBtn = 24
pinRotA = 26
pinRotB = 19
pinPir = 5

inputs = (pinPushBtn, pinRotBtn, pinRotA, pinRotB, pinPir)

GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Outputs
pinLedBlue = 12
pinLedRed = 16
pinLedYellow = 20
pinLedGreen = 21
pinBuzzer = 23

outputs = (pinLedBlue, pinLedRed, pinLedYellow, pinLedGreen, pinBuzzer)
leds = (pinLedBlue, pinLedRed, pinLedYellow, pinLedGreen)

GPIO.setup(outputs, GPIO.OUT)

# Definitions
led = 0
start = False

def DimAllLeds():
    for led in leds:
        GPIO.output(led, False)

def UpdateLeds():
    global led

    if led > len(leds) - 1:
        led = 0

    if led < 0:
        led = len(leds) - 1

    DimAllLeds()
    GPIO.output(leds[led], True)


def ChangeLed(statusRotB):
    global led
    global start

    if start:
        if statusRotB:
            led += 1
        else:
            led -= 1

        UpdateLeds()


# Callbacks
def TurnRotSensor(channel):
    statusRotB = GPIO.input(pinRotB)
    ChangeLed(statusRotB)

def Run(channel):
    global start
    global led
    start = not start

    if start:
        led = 0
        UpdateLeds()
    else:
        DimAllLeds()


GPIO.add_event_detect(pinRotA, GPIO.RISING, callback=TurnRotSensor, bouncetime=50)
GPIO.add_event_detect(pinRotBtn, GPIO.RISING, callback=Run, bouncetime=200)

DimAllLeds()

while True:
    root.update()

    