#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.1                                        ##
#############################################################

'''
7-1) Schrijf een programma dat weergeeft (print en/of GUI) hoeveel milliseconden je een drukknop, 
    verbonden met je RP, had ingedrukt. 
    Je kan deze waarde updaten bij het loslaten.
'''

from tkinter import Tk, Label

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 9 - Oef 7.1')
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
time = False
elapsedTime = 0
prevElapsedTime = 0


# Callbacks
def toggle_timer():
    global time
    time = not time

GPIO.add_event_detect(pinPushBtn, GPIO.BOTH, callback=toggle_timer, bouncetime=50)


# GUI
lblText = Label(root, text="Elapsed time :", padx=10, pady=10)
lblText.grid(row=0, column=0)
lblTime = Label(root, text=elapsedTime, padx=10, pady=10)
lblTime.grid(row=0, column=1)


while True:
    root.update()

