##############################################################
##  Wesley Vercoutere                                       ##
##  CVO Focus : Programmeren                                ##
##  Deel 1: Basis programmeren in Python met Raspberry Pi   ##
##  Eindopdracht : XXX                                      ##
##############################################################

from tkinter import *
import time
import threading
import os

try:
    import RPi.GPIO as GPIO
except:
    print('Not running on a Raspberry, IO is simulated!')
    import RPiMock.GPIO as GPIO


class Bootstrap:

    def __init__(self):
        self.setup_io()
        threading.Thread(target=self.run_io).start()
        
        self.run_frontend()

    def setup_io(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)

    def run_io(self):
        while True:
            GPIO.output(26, GPIO.HIGH)
            time.sleep(1)

            GPIO.output(26, GPIO.LOW)
            time.sleep(1)

    def run_frontend(self):
        root = Tk()
        root.title('Title of program')
        #root.iconbitmap('c:/gui/codemy.ico')
        #root.geometry("600x400")
        #root.state('zoomed')   #window maximized in windows
        #root.attributes('-zoomed', True)   #window maximized in rpi
        #root.attributes('-fullscreen', True)   #window full screen
        #print(f'osname = {os.name}') # windows = nt / raspberry pi = posix

        if (os.name == "nt"):
            root.state('zoomed')
        elif (os.name == "posix"):
            root.attributes('-zoomed', True)

        root.mainloop()


if __name__ == '__main__':
    Bootstrap()