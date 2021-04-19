#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 2: IO met PCF8574                           #
#                                                       #
#  v0.1.0: start                                        #
#  v0.1.1: add interrupt                                #
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

"""
Helper methods

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def is_set(value, bit):
    return value & 1 << bit != 0
"""

import RPi.GPIO as GPIO
import smbus
import time


class Main:

    def __init__(self):
        self.ledRed = 26
        self.ledGreen = 19
        self.ledBlue = 13
        self.ledYellow = 6
        self.leds = (self.ledRed, self.ledGreen, self.ledBlue, self.ledYellow)

        self.btn1 = 21
        self.btn2 = 20
        self.btn3 = 16
        self.btn4 = 12
        self.btns = (self.btn1, self.btn2, self.btn3, self.btn4)

        self.ledRed1 = 0
        self.ledGreen1 = 1
        self.ledBlue1 = 2
        self.ledYellow1 = 3
        self.leds1 = (self.ledRed1, self.ledGreen1, self.ledBlue1, self.ledYellow1)

        self.btn5 = 4
        self.btn6 = 5
        self.btn7 = 6
        self.btn8 = 7
        self.btns1 = (self.btn5, self.btn6, self.btn7, self.btn8)

        self.interruptPin = 23

        self.pcfAddress = 0x20
        self.pcfMessage = 15
        self.bus = None

        self.setup()
        self.initCallbacks()
        self.loop()

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.leds, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.interruptPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.bus = smbus.SMBus(1)
        self.bus.write_byte(self.pcfAddress, self.pcfMessage)

    def initCallbacks(self):
        for i in self.btns:
            GPIO.add_event_detect(i, edge=GPIO.RISING, callback=self.toggleLed, bouncetime=200)
        
        GPIO.add_event_detect(self.interruptPin, edge=GPIO.RISING, callback=self.readI2C, bouncetime=200)

        
    def toggleLed(self, channel):
        print(channel)

    def readI2C(self, channel):
        print(channel)

    def loop(self):
        while True:
            
            print(GPIO.input(self.interruptPin))
            time.sleep(0.5)

            # self.pcfMessage = self.bus.read_byte(self.pcfAddress)

            # for i in range(len(self.btns)):
            #     if GPIO.input(self.btns[i]):
            #         statusLed = self.is_set(self.pcfMessage, self.leds1[i])
            
            #         if statusLed:
            #             self.pcfMessage = self.clear_bit(self.pcfMessage, self.leds1[i])
                    
            #         else:
            #             self.pcfMessage = self.set_bit(self.pcfMessage, self.leds1[i])

            #         time.sleep(0.2)

            # for i in range(len(self.btns1)):
            #     if self.is_set(self.pcfMessage, self.btns1[i]):
            #         GPIO.output(self.leds[i], not GPIO.input(self.leds[i]))
            #         time.sleep(0.2)

            # self.bus.write_byte(self.pcfAddress, self.pcfMessage)

    def set_bit(self, value, bit):
        return value | (1 << bit)

    def clear_bit(self, value, bit):
        return value & ~(1 << bit)

    def is_set(self, value, bit):
        return value & 1 << bit != 0


if __name__ == '__main__':
    Main()
