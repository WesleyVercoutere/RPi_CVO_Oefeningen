#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 2: IO met PCF8574                           #
#                                                       #
#  v0.1.0: start                                        #
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
"""

import RPi.GPIO as GPIO


class Main:

    def __init__(self):
        self.setup()
        self.runLoop()

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup

    def runLoop(self):
        while True:
            pass


if __name__ == '__main__':
    Main()
