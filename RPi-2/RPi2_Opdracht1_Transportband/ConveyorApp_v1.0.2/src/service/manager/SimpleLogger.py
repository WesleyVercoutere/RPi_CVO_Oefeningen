from util.observer.Observer import Observer


class SimpleLogger(Observer):

    def __init__(self, conveyorManager):
        conveyorManager.addObserver(self)

    def update(self, *args, **kwargs):
        message = kwargs["message"]

        print(message)
