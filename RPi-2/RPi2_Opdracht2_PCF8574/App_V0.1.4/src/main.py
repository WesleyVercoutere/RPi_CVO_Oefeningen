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
from hardware.DigitalInputPCF8574 import DigitalInputPCF8574
from hardware.DigitalOutputGPIO import DigitalOutputGPIO
from hardware.DigitalOutputPCF8574 import DigitalOutputPCF8574
from hardware.PCF8574 import PCF8574


class Main:

    def __init__(self):
        self._setup()
        self._initIO()
        self._initCallbacks()
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

        self._btn1GPIO = DigitalInputGPIO(21)
        self._btn2GPIO = DigitalInputGPIO(20)
        self._btn3GPIO = DigitalInputGPIO(16)
        self._btn4GPIO = DigitalInputGPIO(12)

        # PCF8574 IO
        self._pcf8574 = PCF8574(0x20)

        self._ledRedPCF8574 = DigitalOutputPCF8574(0)
        self._ledGreenPCF8574 = DigitalOutputPCF8574(1)
        self._ledBluePCF8574 = DigitalOutputPCF8574(2)
        self._ledYellowPCF8574 = DigitalOutputPCF8574(3)

        self._btn1PCF8574 = DigitalInputPCF8574(4)
        self._btn2PCF8574 = DigitalInputPCF8574(5)
        self._btn3PCF8574 = DigitalInputPCF8574(6)
        self._btn4PCF8574 = DigitalInputPCF8574(7)

        self._interrupt = DigitalInputGPIO(18)

    def _initCallbacks(self):
        self._btn1GPIO.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledRedPCF8574.toggle(), bouncetime=200)
        self._btn2GPIO.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledGreenPCF8574.toggle(), bouncetime=200)
        self._btn3GPIO.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledBluePCF8574.toggle(), bouncetime=200)
        self._btn4GPIO.setEvent(edge=GPIO.RISING, callback=lambda _: self._ledYellowPCF8574.toggle(), bouncetime=200)

        # self._btn1PCF8574.setEvent(callback=lambda _: self._ledRedGPIO.toggle())
        # self._btn2PCF8574.setEvent(callback=lambda _: self._ledGreenGPIO.toggle())
        # self._btn3PCF8574.setEvent(callback=lambda _: self._ledBlueGPIO.toggle())
        # self._btn4PCF8574.setEvent(callback=lambda _: self._ledYellowGPIO.toggle())

        # self._interrupt.setEvent(edge=GPIO.FALLING, callback=self._togglePCFLeds, bouncetime=0)

    def _togglePCFLeds(self):
        self._btn1PCF8574.runCallback()
        self._btn2PCF8574.runCallback()
        self._btn3PCF8574.runCallback()
        self._btn4PCF8574.runCallback()

    def _loop(self):
        while True:
            pass


if __name__ == '__main__':
    Main()

