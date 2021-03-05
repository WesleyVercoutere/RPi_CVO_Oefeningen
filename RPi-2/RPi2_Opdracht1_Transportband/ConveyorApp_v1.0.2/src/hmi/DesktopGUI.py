from tkinter import Tk

from service.observer.Observer import Observer


class DesktopGUI(Observer):

    def __init__(self, conveyorManager):
        conveyorManager.addObserver(self)

        self.root = Tk()
        self.root.title('Transportband')
        self.root.geometry('800x400')

    def update(self, *args, **kwargs):
        pass

    def loop(self):
        self.root.mainloop()
