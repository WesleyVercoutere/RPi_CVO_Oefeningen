from hardware.PulseGenerator import PulseGenerator
from service.observer.Observer import Observer


class LedManager(Observer):

    def __init__(self, leds, conveyorManager):
        self.leds = leds
        self.ledPulse = PulseGenerator(0.5)

        conveyorManager.addObserver(self)

    def notify(self, *args, **kwargs):
        pass

    def loop(self):
        self.ledPulse.generate()

        if self.ledPulse.Q:
            for led in self.leds:
                led.toggle()
