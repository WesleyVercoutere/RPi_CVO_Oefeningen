from tkinter import Tk

class GUI:

    def __init__(self, thermostatManager):
        self.thermostatMgr = thermostatManager

        self.init()

    def init(self):
        self.root = Tk()
        self.root.title('Thermostaat')
        self.root.geometry('800x400')




    def loop(self):
        self.root.update()