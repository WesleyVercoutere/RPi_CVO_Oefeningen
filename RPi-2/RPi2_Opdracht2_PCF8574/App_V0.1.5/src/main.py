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
#                                                       #
#  v0.1.3: Include pcf8574                              #
#  v0.1.4: pcf8574 class                                #
#  v0.1.5: split main class                             #
#########################################################

"""
Verbind 4 leds met je RP en 4 met je PCF8574, verbind ook 4 drukknoppen met je RP en 4 met je PCF8574.
Zorg er nu voor dat de drukkknoppen van de RP de leds van de PCF8574 sturen en omgekeerd.
"""


"""
    Drukknop Pi 1 	    : GPIO 21
    Drukknop Pi 2 	    : GPIO 20
    Drukknop Pi 3 	    : GPIO 16
    Drukknop Pi 4 	    : GPIO 12
    Led Pi Red 	        : GPIO 26
    Led Pi Green 	    : GPIO 19
    Led Pi Blue 	    : GPIO 13
    Led Pi Yellow 	    : GPIO 6
    
    Drukknop PCF8574 1 	: P4
    Drukknop PCF8574 2 	: P5
    Drukknop PCF8574 3 	: P6
    Drukknop PCF8574 4	: P7
    Led PCF8574 Red 	: P0
    Led PCF8574 Green	: P1
    Led PCF8574 Blue	: P2
    Led PCF8574 Yellow 	: P3
    PCF8574 interrupt   : GPIO18
"""

import RPi.GPIO as GPIO

from hardware.DigitalInputGPIO import DigitalInputGPIO
from hardware.DigitalOutputGPIO import DigitalOutputGPIO


class Main:

    def __init__(self):
        self._setup()
        self._initIO()
        self._loop()

    def _setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def _initIO(self):
        # GPIO IO
        self._ledRedGPIO = DigitalOutputGPIO(26)
        self._ledGreenGPIO = DigitalOutputGPIO(19)
        self._ledBlueGPIO = DigitalOutputGPIO(13)
        self._ledYellowGPIO = DigitalOutputGPIO(6)

        self._btn1GPIO = DigitalInputGPIO(21, GPIO.PUD_UP)
        self._btn2GPIO = DigitalInputGPIO(20, GPIO.PUD_UP)
        self._btn3GPIO = DigitalInputGPIO(16, GPIO.PUD_UP)
        self._btn4GPIO = DigitalInputGPIO(12, GPIO.PUD_UP)

    def _loop(self):
        while True:
            pass


if __name__ == '__main__':
    Main()

