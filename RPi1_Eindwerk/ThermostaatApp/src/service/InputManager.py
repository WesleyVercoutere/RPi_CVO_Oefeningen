import RPi.GPIO as GPIO
from DigitalInput import DigitalInput
from TemperatureSensor import TemperatureSensor


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
        self.rotA = DigitalInput(26)
        self.rotB = DigitalInput(19)

    def setTemperatureSensor(self):
        self.tempSensor = TemperatureSensor()