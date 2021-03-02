from domain import ConveyorState as ConveyorState
from domain import PositionState as PositionState
from hardware.PulseGenerator import PulseGenerator
from service.observer.Observer import Observer


class LedSignal(Observer):

    def __init__(self, leds, conveyorManager):
        self.leds = leds
        self.ledPulse = PulseGenerator(0.5)

        conveyorManager.addObserver(self)

    def update(self, *args, **kwargs):
        conveyor = kwargs["conveyor"]
        self.resetLeds()
        self.controlPositionState(conveyor)
        self.controlConveyorState(conveyor)

    def controlPositionState(self, conveyor):
        if conveyor.position.id == PositionState.HOME:
            self.leds[0].setOutput(True)

        if conveyor.position.id == PositionState.POSITION_1:
            self.leds[1].setOutput(True)

        if conveyor.position.id == PositionState.POSITION_2:
            self.leds[1].setOutput(True)

    def controlConveyorState(self, conveyor):
        if conveyor.state == ConveyorState.MOVING_TO_HOME_POSITION:
            self.leds[0].blink = True

        if conveyor.state == ConveyorState.MOVING_TO_POSITION_1:
            self.leds[1].blink = True

        if conveyor.state == ConveyorState.MOVING_TO_POSITION_2:
            self.leds[2].blink = True

        if conveyor.state == ConveyorState.SET_POSITION_GENERAL:
            self.leds[3].blink = True
        
        if conveyor.state == ConveyorState.SET_POSITION_1:
            self.leds[1].blink = True
            self.leds[3].setOutput(True)

        if conveyor.state == ConveyorState.SET_POSITION_2:
            self.leds[2].blink = True
            self.leds[3].setOutput(True)

    def resetLeds(self):
        for led in self.leds:
            led.blink = False
            led.setOutput(False)

    def loop(self):
        self.ledPulse.generate()

        if self.ledPulse.Q:
            for led in self.leds:
                if led.blink:
                    led.toggle()
