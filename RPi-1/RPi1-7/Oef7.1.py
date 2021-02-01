#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 7 - Oef 1                                          ##
#############################################################

'''
Stuur met een GUI een led verbonden met GPIO 25. 
Plaats een knop ON en een knop OFF op je GUI
'''

from tkinter import Tk, Button

try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)


root = Tk()
root.title('Les 7 - Oef 1')
root.geometry('800x400')

led = 25
ledStatus = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)

def On():
    global ledStatus
    ledStatus = True

def Off():
    global ledStatus
    ledStatus = False

btnOn = Button(root, text="On", command=On, padx=5, pady=5)
btnOff = Button(root, text="Off", command=Off, padx=5, pady=5)
btnOn.grid(row=0, column=0, padx=5, pady=5)
btnOff.grid(row=0, column=1, padx=5, pady=5)

while True:
    GPIO.output(led, ledStatus)
    root.update()
