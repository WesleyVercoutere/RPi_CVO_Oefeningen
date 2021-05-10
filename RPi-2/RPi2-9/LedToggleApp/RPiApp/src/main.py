import RPi.GPIO as GPIO

from hardware.DigitalInputGPIO import DigitalInputGPIO
from hardware.DigitalOutputGPIO import DigitalOutputGPIO


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

        self._btn1GPIO = DigitalInputGPIO(21, GPIO.PUD_UP)
        self._btn2GPIO = DigitalInputGPIO(20, GPIO.PUD_UP)
        self._btn3GPIO = DigitalInputGPIO(16, GPIO.PUD_UP)
        self._btn4GPIO = DigitalInputGPIO(12, GPIO.PUD_UP)

    def _initCallbacks(self):
        self._btn1GPIO.setEvent(edge=GPIO.FALLING, callback=self._ledRedGPIO.toggle, bouncetime=200)
        self._btn2GPIO.setEvent(edge=GPIO.FALLING, callback=self._ledGreenGPIO.toggle, bouncetime=200)
        self._btn3GPIO.setEvent(edge=GPIO.FALLING, callback=self._ledBlueGPIO.toggle, bouncetime=200)
        self._btn4GPIO.setEvent(edge=GPIO.FALLING, callback=self._ledYellowGPIO.toggle, bouncetime=200)

    def _loop(self):
        while True:
            pass
    
if __name__ == "__main__":
    Main()