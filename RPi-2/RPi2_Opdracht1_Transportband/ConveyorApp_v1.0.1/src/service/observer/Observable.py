class Observable:

    def __init__(self):
        self.observers = []
    
    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self, arg):
        for observer in self.observers:
            observer.update(arg)
