import RPi.GPIO as GPIO

from hardware.DigitalInput import DigitalInput
from hardware.TemperatureSensor import TemperatureSensor
from hardware.RotaryEncoder import RotaryEncoder


class InputManager:

    def __init__(self):
        self.init()

    def init(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.setDigitalInputs()
        self.setTemperatureSensor()

    def setDigitalInputs(self):
        self.btn1 = DigitalInput(21)
        self.btn2 = DigitalInput(16)
        self.btnRot = DigitalInput(20)
        self.rotary = RotaryEncoder(26, 19)

    def setTemperatureSensor(self):
        self.tempSensor = TemperatureSensor()

    def getTemp(self):
        return self.tempSensor.readTemp()

    def setCallback(self, input, callback, bouncetime=200):
        input.clearEvent()
        input.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=bouncetime)

    def clearCallback(self, input):
        input.clearEvent()
