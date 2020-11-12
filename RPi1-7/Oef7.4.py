#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 7 - Oef 4                                          ##
#############################################################

'''
Gebruik een slider om de knippersnelheid van je LED in te stellen tussen 1 en 10 keer per seconde
'''

from tkinter import Tk, Button, Label, Scale
import time

try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)


root = Tk()
root.title('Les 7 - Oef 4')
root.geometry('800x400')

led = 25
ledStatus = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

slider = Scale(root, from_= 1, to = 10, orient="horizontal")
slider.grid(row=0, column=0, padx=5, pady=5)

def Toggle():
    global ledStatus
    ledStatus = not ledStatus

startTime = time.time()

while True:
    currentTime = time.time()

    if currentTime >= (startTime + int(slider.get())):
        startTime = time.time()
        Toggle()
        

    GPIO.output(led, ledStatus)
    root.update()
