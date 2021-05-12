import RPi.GPIO as GPIO
import time
import serial

from tkinter import *


class Main:

    def __init__(self):
        self._leds = [26, 19, 13, 6]
        self._ledsStatus = [False, False, False, False]
        self._btns = [21, 20, 16, 12]

        self._setup()
        self._initIO()
        self._initCallbacks()
        self._initGui()
        self._initBT()
        self._loop()
        
    def _setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def _initIO(self):
        GPIO.setup(self._leds, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self._btns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _initCallbacks(self):
        GPIO.add_event_detect(self._btns[0], edge=GPIO.RISING, callback=lambda _: self._toggleLed(0), bouncetime=200)
        GPIO.add_event_detect(self._btns[1], edge=GPIO.RISING, callback=lambda _: self._toggleLed(1), bouncetime=200)
        GPIO.add_event_detect(self._btns[2], edge=GPIO.RISING, callback=lambda _: self._toggleLed(2), bouncetime=200)
        GPIO.add_event_detect(self._btns[3], edge=GPIO.RISING, callback=lambda _: self._toggleLed(3), bouncetime=200)

    def _toggleLed(self, index):
        self._ledsStatus[index] = not self._ledsStatus[index]
        self._update()

    def _update(self):
        for i in range(len(self._leds)):
            GPIO.output(self._leds[i], self._ledsStatus[i])

    def _initGui(self):
        self.root = Tk()
        self.root.title('Leds')

        frame = LabelFrame(self.root, text = "Led buttons", padx=10, pady=10)

        for i in range(4):
            frame.columnconfigure(i, minsize=150, weight=1)

        btn_red = Button(frame, text="Red", command=lambda: self._toggleLed(0))
        btn_red.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

        btn_green = Button(frame, text="Green", command=lambda: self._toggleLed(1))
        btn_green.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

        btn_blue = Button(frame, text="Blue", command=lambda: self._toggleLed(2))
        btn_blue.grid(column=2, row=0, padx=10, pady=10, sticky='ew')

        btn_yellow = Button(frame, text="Yellow", command=lambda: self._toggleLed(3))
        btn_yellow.grid(column=3, row=0, padx=10, pady=10, sticky='ew')

        frame.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    def _initBT(self):
        self.port = serial.Serial("/dev/ttyS0",9600)

    def _handleBT(self, msg):
        if msg == 'red':
            self._toggleLed(0)

        elif msg == 'green':
            self._toggleLed(1)

        elif msg == 'blue':
            self._toggleLed(2)

        elif msg == 'yellow':
            self._toggleLed(3)

        else:
            return

    def _loop(self):
        c=0
        # msg=[]  dan komen alle bytes in een list  bij msg=b"" komen alle bytes in een byte string
        msg=b""
        msgstr=""

        while True:
            self.root.update()

            if self.port.inWaiting()>0:
                c = self.port.read()  # komt binnen als byte
                
                if c == b'\n':
                    msgstr=msg.decode()  # 
                    self._handleBT(msgstr)
                    msg=b""
                    msgstr=""

                elif c==b'\r':
                    pass

                else:
                    msg += c  # add byte aan byte string

    
if __name__ == "__main__":
    main = Main()