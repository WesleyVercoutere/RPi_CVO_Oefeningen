from tkinter import *

try:
    import RPi.GPIO as GPIO
except:
    import DummyGPIO as GPIO


root = Tk()
root.title = "Led on/off"
root.geometry("800x400")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def ledOn():
    GPIO.output(25, GPIO.HIGH)

def ledOff():
    GPIO.output(25, GPIO.LOW)

btnOn = Button(root, text="On", command=ledOn)
btnOn.place(x=10, y=10)

btnOff = Button(root, text="Off", command=ledOff)
btnOff.place(x=50, y=10)



root.mainloop()
