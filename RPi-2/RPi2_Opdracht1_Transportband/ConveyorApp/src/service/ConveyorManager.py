import RPi.GPIO as GPIO

class ConveyorManager:

    def __init__(self, hardwareManager):
        self.hardwareMgr = hardwareManager

        self.setCallbacks()

    def setCallbacks(self):
        self.hardwareMgr.btn1.setEvent(GPIO.RISING, lambda _ : self.toggleLed(), 200)

    def toggleLed(self):
        self.hardwareMgr.ledGreen.toggle()
