from tkinter import Tk

try:
    import RPi.GPIO as GPIO
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


root = Tk()
root.title('Les 7 - Oef 1')
root.geometry('800x400')

# GPIO general
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Inputs
pinPushBtn = 25
statusPushBtn = False
prevStatusPushBtn = False
pinRotBtn = 24
statusRotBtn = False
prevStatusRotBtn = False
pinRotA = 26
statusRotA = False
prevStatusRotA = False
pinRotB = 19
statusRotB = False
prevStatusRotB = False
pinPir = 5
statusPir = False
prevStatusPir = False

inputs = (pinPushBtn, pinRotBtn, pinRotA, pinRotB, pinPir)
statusInputs = [statusPushBtn, statusRotBtn, statusRotA, statusRotB, statusPir] 
prevStatusInputs = [prevStatusPushBtn, prevStatusRotBtn, prevStatusRotA, prevStatusRotB, prevStatusPir] 

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


# Definitions
def ReadInputs():
    global statusRotA
    global statusRotB
    statusRotA = GPIO.input(pinRotA)
    statusRotB = GPIO.input(pinRotB)


def SetPrevStatus():
    global statusRotA
    global statusRotB
    global prevStatusRotA
    global prevStatusRotB
    prevStatusRotA = statusRotA
    prevStatusRotB = statusRotB

# Program loop
while True:
    root.update()

    ReadInputs()


    # if statusRotA != prevStatusRotA:
    #     print(f"status A {statusRotA}, status B {statusRotB}")

    # if statusRotB != prevStatusRotB:
    #     print(f"status B {statusRotB}, status A {statusRotA}")

    if statusRotA and (statusRotA != prevStatusRotA):
        if statusRotB:
            print("cw")
        else:
            print("ccw")

    SetPrevStatus()

