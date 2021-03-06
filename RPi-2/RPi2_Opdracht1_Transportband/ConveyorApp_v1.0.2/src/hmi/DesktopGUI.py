from tkinter import Tk

from util.observer import Observer


class DesktopGUI(Observer):

    def __init__(self, conveyorManager):
        self.root = None

        conveyorManager.addObserver(self)
        self.setupRoot()
        self.setupLabels()
        self.setupButtons()

    def setupRoot(self):
        self.root = Tk()
        self.root.title('Transportband')
        self.root.geometry('800x400')

    def setupLabels(self):
        pass

    def setupButtons(self):
        pass

    def update(self, *args, **kwargs):
        pass

    def loop(self):
        self.root.mainloop()
