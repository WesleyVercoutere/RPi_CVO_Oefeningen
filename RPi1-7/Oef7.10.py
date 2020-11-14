#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 7 - Oef 10                                         ##
#############################################################

'''
Maak een programma dat je rotary encoder volgt en een getal tussen 0-255 op je GUI aanpast.
Draaien naar links getal vermindert.
Draaien naar rechts getal vermeerdert.
Bv met stapjes van +/-5
'''

from tkinter import Tk, Label

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 7 - Oef 10')
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

GPIO.setup(outputs, GPIO.OUT, initial=GPIO.LOW)


# Definitions
number = 0
MIN_NUMBER = 0
MAX_NUMBER = 255
STEP = 5


# Callbacks
def UpdateNumber(arg):
    global number

    if arg:
        number += STEP
    else:
        number -= STEP

    if number > MAX_NUMBER:
        number = MIN_NUMBER
    
    if number < MIN_NUMBER:
        number = MAX_NUMBER


def TurnRotSensor(channel):
    statusRotB = GPIO.input(pinRotB)
    UpdateNumber(statusRotB)


# GUI
label = Label(root, text=str(number))
label.place(x=10, y=10)


GPIO.add_event_detect(pinRotA, GPIO.RISING, callback=TurnRotSensor, bouncetime=50)


while True:
    root.update()
    label['text'] = number 
