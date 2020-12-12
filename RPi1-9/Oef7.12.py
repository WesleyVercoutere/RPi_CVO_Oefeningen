#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.12                                       ##
#############################################################

'''
7.12) Stuur je servo-motor van links nar rechts met je GUI schuifregelaar en 3 knoppen ( -90/0/+90)
'''

from tkinter import Tk, Label, Entry, Button

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


# Outputs
servo = 18

GPIO.setup(servo, GPIO.OUT)
p = GPIO.PWM(servo, 50)  # channel=18  frequency=50Hz
p.start(7.5)

dc = 0
prevDc = 0


#Callback
def move_servo(position):
    p.ChangeDutyCycle(float(position))


# GUI
Label(root, text="Duty cycle :", padx=10, pady=10).grid(row=0, column=0)
inDc = Entry(root)
inDc.grid(row=0, column=1)

btnMove = Button(root, text="Move Servo", command = lambda: move_servo(inDc.get()), padx=5, pady=5)
btnMove.grid(row=0, column=2)



while True:
    root.update()
