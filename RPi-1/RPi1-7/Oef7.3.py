#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 7 - Oef 3                                          ##
#############################################################

'''
Herhaal oef 1 en 2 en toon in de GUI de status van een LED ( 0 of 1) in een label
'''

from tkinter import Tk, Button, Label, StringVar

try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)


root = Tk()
root.title('Les 7 - Oef 3')
root.geometry('800x400')

led = 25
ledStatus = False

ledStatusLabelPrefix = "Status van led = "
ledStatusLabelText = StringVar()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

label = Label(root, textvariable=ledStatusLabelText)
label.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="W")

def SetLabelText():
    global ledStatusLabelText
    global ledStatusLabelPrefix
    global ledStatus

    ledStatusLabelText.set(ledStatusLabelPrefix + str(ledStatus))

def On():
    global ledStatus
    ledStatus = True
    SetLabelText()

def Off():
    global ledStatus
    ledStatus = False
    SetLabelText()

def Toggle():
    global ledStatus
    ledStatus = not ledStatus
    SetLabelText()

btnOn = Button(root, text="On", command=On, padx=5, pady=5)
btnOff = Button(root, text="Off", command=Off, padx=5, pady=5)
btnToggle = Button(root, text="Toggle", command=Toggle, padx=5, pady=5)
btnOn.grid(row=0, column=0, padx=5, pady=5)
btnOff.grid(row=0, column=1, padx=5, pady=5)
btnToggle.grid(row=0, column=2, padx=5, pady=5)
SetLabelText()

while True:
    GPIO.output(led, ledStatus)
    root.update()
