from service.observer.Observer import Observer


class LedManager(Observer):

    def __init__(self, leds, conveyorManager):
        self.leds = leds

        conveyorManager.addObserver(self)

    def notify(self, *args, **kwargs):
        pass

    def loop(self):
        pass
