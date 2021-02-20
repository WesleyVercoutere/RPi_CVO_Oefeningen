import RPi.GPIO as GPIO

from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, hardwareManager):
        self.hardwareMgr = hardwareManager

        self.setCallbacks()

#region Main methods conveyor

    def moveToHomePosition(self):
        print("Moving to home position")

    def moveToPosition(self, position):
        print(f"Moving to {position}")

    def move(self, direction):
        print(f"Moving {direction}")

    def setPosition(self, positionId, position):
        print(f"Set {positionId} to {position}")

#endregion

    def setCallbacks(self):
        self.hardwareMgr.btn1.setEvent(GPIO.RISING, lambda _ : self.toggleLed(), 200)

    def toggleLed(self):
        self.hardwareMgr.ledGreen.toggle()
