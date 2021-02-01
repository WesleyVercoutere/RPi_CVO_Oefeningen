'''
a / Maak een flexibele sturing voor 3 lampen ( leds) die je bedient met 3 drukknoppen. ( leds+ drukknoppen via 6 GPIO’s)
b/ De toestand van de leds is ook te checken op een GUI. Deze GUI heeft ook 3 drukknoppen om de leds te bedienen.
c/ Het doel is om te kunnen programmeren en opslaan welke led(s) reageren op welke drukknop(pen).
d/ Je Python Programma zal gebruik maken van settings welke in txt-files worden opgeslagen
e/ De settings worden automatisch geladen bij het opstarten van de RP.
f/ Settings kunnen via GUI en via BLT worden ingegeven
'''

import RPi.GPIO as GPIO
import time

class BlackBox:

    btn1 = 5
    btn2 = 6
    btn3 = 13
    buttons = (btn1, btn2, btn3)

    red = 16
    green = 20
    blue = 21
    leds = (red, green, blue)

    def __init__(self):
        self.initGPIO()
        self.initSettings()

        self.checkFile()

    def initGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.leds, GPIO.OUT)

    def initSettings(self):
        file = open("settings.txt", "w")

        file.write("btn1:red")
        file.write("\n")
        file.write("btn2:green")
        file.write("\n")
        file.write("btn3:blue")

        file.close()

    def checkFile(self):
        file = open("settings.txt", "r")

        for line in file:
            print(line)

        file.close()

    def run(self):
        while True:
            
            for btn in self.buttons:
                


            time.sleep(0.05)
        


if __name__ == "__main__":
    bb = BlackBox()
    bb.run()