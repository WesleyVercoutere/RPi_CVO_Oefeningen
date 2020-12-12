#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.3                                        ##
#############################################################

'''
7-3) Schrijf een programma dat een teller verhoogt en ze’n waarde uitprint telkens een schakelaar wordt ingedrukt. 
    Kan je die waarde ook tonen in een GUI? 
    Je kan geen GUI aanpassen vanuit de callback van je schakelaar, hoe los je dit op?
'''

from tkinter import Tk, Label

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 9 - Oef 7.3')
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
counter = 0
prevCounter = 0


# GUI
lblCounterTitle = Label(root, text="Number of times button pushed =", padx=10, pady=10)
lblCounterTitle.grid(row=0, column=0)

lblCounter = Label(root, text="0", padx=10, pady=10)
lblCounter.grid(row=0, column=1)

def update_label():
    lblCounter["text"] = str(counter)


# Callbacks
def update_counter(channel):
    global counter
    counter += 1


GPIO.add_event_detect(pinPushBtn, GPIO.RISING, callback=update_counter, bouncetime=50)


while True:
    root.update()

    if counter != prevCounter:
        prevCounter = counter
        update_label()
