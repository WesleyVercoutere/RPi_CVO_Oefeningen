import RPi.GPIO as GPIO
import time

import hardware.Rotation as Rotation

class StepperMotor:

    def __init__(self, pin1, pin2, pin3, pin4):
        self.channels = (pin1, pin2, pin3, pin4)
        self.steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        
        GPIO.setup(self.channels, GPIO.OUT)

    def rotate(self, direction):
        if direction == Rotation.CLOCKWISE:
            self.rotateClockwise(10)

        if direction == Rotation.COUNTERCLOCKWISE:
            self.rotateCounterclockwise(10)

    def setMotor(self, state):
        for i in range(len(self.channels)):
            GPIO.output(self.channels[i], state[i])

    def rotateCounterclockwise(self, hold):
        for step in range (3,-1, -1):
            self.setMotor(self.steps[step])
            time.sleep(hold/1000)
            
    def rotateClockwise(self, hold):
        for step in range (0,4):
            self.setMotor(self.steps[step])
            time.sleep(hold/1000)

    def stop(self):
        step = [0,0,0,0]
        self.setMotor(step)

