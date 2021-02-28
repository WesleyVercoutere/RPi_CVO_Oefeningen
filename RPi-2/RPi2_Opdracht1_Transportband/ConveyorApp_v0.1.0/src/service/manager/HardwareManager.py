import time

import RPi.GPIO as GPIO

import domain.PositionState as Position
import hardware.Rotation as Rotation
from hardware.DigitalInput import DigitalInput
from hardware.DigitalOutput import DigitalOutput
from hardware.PulseGenerator import PulseGenerator
from hardware.RotaryEncoder import RotaryEncoder
from hardware.StepperMotor import StepperMotor

'''
-	Drukknop 1 : GPIO 18
-	Drukknop 2 : GPIO 23
-	Drukknop 3 : GPIO 25
-	Drukknop 4 : GPIO 12
-	Drukknop 5 : GPIO 16
-	Drukknop 6 : GPIO 26
-	Rotary A : GPIO 20
-	Rotary B : GPIO 21

-	Potentiometer : MCP 3008 channel 1
-	MCP3008 :
    o	CLK : GPIO 11 / SPIO SCLK
    o	Dout : GPIO 9 / SPIO MISO
    o	Din : GPIO 10 / SPIO MOSI
    o	CS/Sh : GPIO 8 / SPIO CS1

-	Led green : GPIO 5
-	Led yellow : GPIO 6
-	Led blue : GPIO 13
-	Led red : GPIO 19

-	Stepper motor
    o	In 1 : GPIO 17
    o	In 2 : GPIO 27
    o	In 3 : GPIO 24
    o	In 4 : GPIO 22

'''


class HardwareManager:

    def __init__(self):
        self.initGPIO()
        self.initDigitalInputs()
        self.initAnalogInputs()
        self.initDigitalOutputs()
        self.initMotor()

        self.nbrOfStepsFromHomePosition = 0
        self.moveMotorCcw = False
        self.moveMotorCw = False

        self.ledPulse = PulseGenerator(0.5)
        self.blink = [False, False, False, False]

    def initGPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def initDigitalInputs(self):
        self.btn1 = DigitalInput(18)
        self.btn2 = DigitalInput(23)
        self.btn3 = DigitalInput(25)
        self.btn4 = DigitalInput(12)
        self.btn5 = DigitalInput(16)
        self.btn6 = DigitalInput(26)
        self.rotBtn = RotaryEncoder(20, 21)

    def initAnalogInputs(self):
        pass

    def initDigitalOutputs(self):
        self.ledGreen = DigitalOutput(5)
        self.ledYellow = DigitalOutput(6)
        self.ledBlue = DigitalOutput(13)
        self.ledRed = DigitalOutput(19)

        self.leds = (self.ledGreen, self.ledYellow, self.ledBlue, self.ledRed)

    def initMotor(self):
        self.motor = StepperMotor(17, 27, 24, 22)

    def setConveyor(self, conveyor):
        self.conveyor = conveyor

    def setCallbacks(self):
        self.btn1.setEvent(GPIO.RISING, lambda _: self.conveyor.homePositionReached(), 200)
        self.btn2.setEvent(GPIO.RISING, lambda _: self.conveyor.move(Rotation.COUNTERCLOCKWISE), 200)
        self.btn3.setEvent(GPIO.RISING, lambda _: self.conveyor.move(Rotation.CLOCKWISE), 200)
        self.btn4.setEvent(GPIO.RISING, lambda _: self.conveyor.moveToPosition(Position.POSITION_1), 200)
        self.btn5.setEvent(GPIO.RISING, lambda _: self.conveyor.moveToPosition(Position.POSITION_2), 200)
        self.btn6.setEvent(GPIO.RISING, lambda _: self.conveyor.setPosition(), 200)
        self.rotBtn.setEvent(GPIO.RISING, self.conveyor.move)

    def setHomePosition(self):
        self.nbrOfStepsFromHomePosition = 0

    def motorRotate(self, direction):
        if direction == Rotation.CLOCKWISE:
            self.moveMotorCcw = False
            self.moveMotorCw = True

        if direction == Rotation.COUNTERCLOCKWISE:
            self.moveMotorCcw = True
            self.moveMotorCw = False

    def motorRotateOneStep(self, direction):
        self.motor.rotate(direction)
        self.nbrOfStepsFromHomePosition += direction

    def motorStop(self):
        self.moveMotorCcw = False
        self.moveMotorCw = False
        self.motor.stop()

    def toggleBlinkLed(self, color):
        self.blink[color] = True

    def ledHigh(self, color):
        self.leds[color].setOutput(True)

    def resetLeds(self):
        for i in range(len(self.blink)):
            self.blink[i] = False

        for led in self.leds:
            led.setOutput(False)

    def loop(self):
        while True:
            self.ledPulse.generate()

            for i in range(len(self.blink)):
                if self.blink[i] and self.ledPulse.Q:
                    self.leds[i].toggle()

            if self.moveMotorCw:
                self.motorRotateOneStep(Rotation.CLOCKWISE)
                self.conveyor.positionReached()

            if self.moveMotorCcw:
                self.motorRotateOneStep(Rotation.COUNTERCLOCKWISE)
                self.conveyor.positionReached()
                
            time.sleep(0.01)
