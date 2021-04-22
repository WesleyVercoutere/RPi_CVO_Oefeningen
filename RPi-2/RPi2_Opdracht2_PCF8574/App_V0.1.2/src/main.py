#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 2: IO met PCF8574                           #
#                                                       #
#  v0.1.0: start                                        #
#  v0.1.1: add interrupt                                #
#  v0.1.2: add classes DigitalInput, DigitalOutput      #
#       Zonder pcf8574 IO                               #
#########################################################

"""
    Drukknop Pi 1 	    : GPIO 21
    Drukknop Pi 2 	    : GPIO 20
    Drukknop Pi 3 	    : GPIO 16
    Drukknop Pi 4 	    : GPIO 12
    Led Pi Red 	        : GPIO 26
    Led Pi Green 	    : GPIO 19
    Led Pi Blue 	    : GPIO 13
    Led Pi Yellow 	    : GPIO 6

    Om de opbouw duidelijk te maken is de pcf8574 io uit deze versie weg gelaten
    Deze wordt opnieuw toegevoegd in V0.1.3
"""

import RPi.GPIO as GPIO

from hardware.DigitalInput import DigitalInput
from hardware.DigitalOutput import DigitalOutput


class Main:

    def __init__(self):
        self._setup()

        self._ledRed = DigitalOutput(26)
        self._ledGreen = DigitalOutput(19)
        self._ledBlue = DigitalOutput(13)
        self._ledYellow = DigitalOutput(6)
        self._leds = (DigitalOutput(26), DigitalOutput(19), DigitalOutput(13), DigitalOutput(6))

        self._btn1 = DigitalInput(21)
        self._btn2 = DigitalInput(20)
        self._btn3 = DigitalInput(16)
        self._btn4 = DigitalInput(12)
        self._buttons = (DigitalInput(21), DigitalInput(20), DigitalInput(16), DigitalInput(12))

        self._initCallbacks()
        self._loop()

    def _setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def _initCallbacks(self):
        for i in range(len(self._buttons)):
            self._buttons[i].setEvent(edge=GPIO.RISING, callback=lambda x: self._leds[i].toggle(), bouncetime=200)

        # self._btn1.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledRed.toggle(), bouncetime=200)
        # self._btn2.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledGreen.toggle(), bouncetime=200)
        # self._btn3.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledBlue.toggle(), bouncetime=200)
        # self._btn4.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledYellow.toggle(), bouncetime=200)

    def _loop(self):
        while True:
            pass


if __name__ == '__main__':
    Main()

