import RPi.GPIO as GPIO


class InputManager:

    def __init__(self, buttons, rotary):
        self.buttons = buttons
        self.rotary = rotary

        self.conveyorMgr = None
        self.motorMgr = None

    def setManagers(self, conveyorManager, motorManager):
        self.conveyorMgr = conveyorManager
        self.motorMgr = motorManager

    def setCallbacks(self):
        self.buttons[0].setEvent(GPIO.RISING, lambda _: self.btn1Pressed(), 200)
        self.buttons[1].setEvent(GPIO.RISING, lambda _: self.btn2Pressed(), 200)
        self.buttons[2].setEvent(GPIO.RISING, lambda _: self.btn3Pressed(), 200)
        self.buttons[3].setEvent(GPIO.RISING, lambda _: self.btn4Pressed(), 200)
        self.buttons[4].setEvent(GPIO.RISING, lambda _: self.btn5Pressed(), 200)
        self.buttons[5].setEvent(GPIO.RISING, lambda _: self.btn6Pressed(), 200)
        self.rotary.setEvent(GPIO.RISING, self.conveyor.move)

    def btn1Pressed(self):
        pass

    def btn2Pressed(self):
        pass

    def btn3Pressed(self):
        pass

    def btn4Pressed(self):
        pass

    def btn5Pressed(self):
        pass

    def btn6Pressed(self):
        pass

    def loop(self):
        pass
