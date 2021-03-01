from service.observer.Observer import Observer


class DisplayManager(Observer):

    def __init__(self, display, conveyorManager):
        self.display = display

        conveyorManager.addObserver(self)

    def update(self, *args, **kwargs):
        pass

    def loop(self):
        pass
