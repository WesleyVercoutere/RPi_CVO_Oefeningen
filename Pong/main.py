##########################
##  Wesley Vercoutere   ##
##  Python Pong Game    ##
##########################

from tkinter import Tk

class Main:

    def __init__(self):
        self.setupRoot()

    def setupRoot(self):
        self.root = Tk()
        self.root.title("Hello World")
        self.root.geometry("800x400")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()