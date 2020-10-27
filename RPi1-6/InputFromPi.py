from tkinter import *

try:
    import RPi.GPIO as GPIO
except:
    import GPIO


drukknop=18
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(drukknop,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
status_drukknop = GPIO.input(drukknop)
 
root = Tk()
root.title = "Status_drukknop"
root.geometry("800x400")
 
mijnLabel= Label( root, text = status_drukknop)
mijnLabel.place(x=10, y=50)
 
root.mainloop()