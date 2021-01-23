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
       # self.rotA = DigitalInput(26)
       # self.rotB = DigitalInput(19)
        self.rotary = RotaryEncoder(26, 19)

    def setTemperatureSensor(self):
        self.tempSensor = TemperatureSensor()

    def getTemp(self):
        return self.tempSensor.readTemp()

    def setCallbacks(self, callback):
        self.btn1.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=200)
        self.btn2.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=200)
        self.btnRot.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=200)
       # self.rotA.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=200)
       # self.rotB.setEvent(edge=GPIO.RISING, callback=callback, bouncetime=200)
