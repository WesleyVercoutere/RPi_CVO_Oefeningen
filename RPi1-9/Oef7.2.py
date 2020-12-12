#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.2                                        ##
#############################################################

'''
7-2) Schrijf een programma dat een led vanop 4 plaatsen kan aansturen, 
    zowel met 4 GPIO drukknoppen als met 4 GUI knoppen.
'''

from tkinter import Tk, Label, Button

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 9 - Oef 7.2')
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


# Program variables
ledStatus = False

def update_led():
    GPIO.output(pinLedBlue, ledStatus)

# Callbacks
def toggle_status(channel):
    global ledStatus
    ledStatus = not ledStatus

    update_led()

GPIO.add_event_detect(pinPushBtn, GPIO.RISING, callback=toggle_status, bouncetime=50)
GPIO.add_event_detect(pinRotBtn, GPIO.RISING, callback=toggle_status, bouncetime=100)

# GUI
#btn = Button(root, text="Toggle led", command = lambda channel=1: toggle_status(channel), padx=10, pady=10)
#btn.grid(row=0, column=1, padx=10, pady=10)

for i in range(4):
    btn = Button(root, text="Toggle led", command = lambda: toggle_status(i), padx=10, pady=10)
    btn.grid(row=0, column=i, padx=10, pady=10)


while True:
    root.update()

