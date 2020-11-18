##############################################################
##  Wesley Vercoutere                                       ##
##  CVO Focus : Programmeren                                ##
##  Deel 1: Basis programmeren in Python met Raspberry Pi   ##
##  Eindopdracht : XXX                                      ##
##############################################################

import threading
import time
from tkinter import Tk, Button, Label

try:
    import RPi.GPIO as GPIO
except:
    from lib.dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)


root = Tk()
root.title("Test proggie dummy GPIO")
root.geometry("800x400")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
led1 = 1
led2 = 2
led3 = 3

button1 = 11
button2 = 12

leds = (led1, led2, led3)
buttons = (button1, button2)

for led in leds:
    GPIO.setup(led, GPIO.OUT)

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

starTime = time.time()
outputled3 = False

def toggleLed3():
    global starTime
    global outputled3

    currentTime = time.time()

    if currentTime > starTime + 1:
        starTime = time.time()
        outputled3 = not outputled3

def loop():
    global outputled3
    while True:
        GPIO.output(led1, GPIO.input(button1))
        GPIO.output(led2, GPIO.input(button2))
        GPIO.output(led3, outputled3)

        toggleLed3()


label1 = Label(root, text="Button 1: pull down -> led 1")
label1.grid(row=0, column=0)

label2 = Label(root, text="Button 2: pull up -> led 2")
label2.grid(row=1, column=0)

        
threading.Thread(target=loop).start()

root.mainloop()
