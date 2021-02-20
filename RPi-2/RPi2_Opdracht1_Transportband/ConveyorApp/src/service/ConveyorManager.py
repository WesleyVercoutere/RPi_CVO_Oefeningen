import RPi.GPIO as GPIO

from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, hardwareManager):
        self.hardwareMgr = hardwareManager
        self.setHardwareCallbacks()

        self.moveToHomePosition()

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


    def setHardwareCallbacks(self):
        print("Set hardware callbacks")
        callbacks = [self.toggleLed]
        self.hardwareMgr.setCallbacks(callbacks)

    def toggleLed(self):
        print("Toggle led")
        self.hardwareMgr.ledGreen.toggle()
