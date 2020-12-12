#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.12                                       ##
#############################################################

'''
7.12) Stuur je servo-motor van links nar rechts met je GUI schuifregelaar en 3 knoppen ( -90/0/+90)
'''

from tkinter import Tk, Label

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 9 - Oef 7.12')
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


# Callbacks


# GUI



while True:
    root.update()

