class Observable:

    def __init__(self):
        self.observers = []
    
    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
