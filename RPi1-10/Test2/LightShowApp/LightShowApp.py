import RPi.GPIO as GPIO
from rpi_ws281x import *
import time

class LightShowApp:

    def __init__(self):
        self.currentShow = 'idle'
        self.interval = 0.1

        self.initIO()
        self.initCallbacks()
        self.initLedStrip()

    def initIO(self):
        # GPIO general
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Inputs
        self.pinBtn1 = 20
        self.pinBtn2 = 21
        
        inputs = (self.pinBtn1, self.pinBtn2)
        GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def initCallbacks(self):
        GPIO.add_event_detect(self.pinBtn1, GPIO.RISING, callback=lambda channel, arg='show1': self.toggleShow(channel, arg), bouncetime=200)
        GPIO.add_event_detect(self.pinBtn2, GPIO.RISING, callback=lambda channel, arg='show2': self.toggleShow(channel, arg), bouncetime=200)

    def initLedStrip(self):
        # LED strip configuration:
        LED_COUNT      = 8      # Number of LED pixels.
        LED_PIN        = 13  # GPIO pin connected to the pixels (18 uses PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10     # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)  # last par LED_CHANNEL not used 
        self.strip.begin()
        self.resetStrip()

    def toggleShow(self, channel, show):
        if show == 'show1' and self.currentShow != 'show1':
            self.currentShow = 'show1'
        elif show == 'show2' and self.currentShow != 'show2':
            self.currentShow = 'show2'
        else:
            self.currentShow = 'idle'
        
        self.ledIndex = 0
        self.prevLed = -1
        self.startTime = 0
        self.step = 1
        self.resetStrip()

    def resetStrip(self):
        for i in range(8):
            self.strip.setPixelColorRGB(i, 0, 0, 0)
            
        self.strip.show()

    def idle(self):
        pass

    def show1(self):
        if time.time() > (self.startTime + self.interval):
            self.startTime = time.time()
            self.resetStrip()
            self.strip.setPixelColorRGB(self.ledIndex, 5, 5, 5)
            self.strip.show()

            self.ledIndex += 1

            if self.ledIndex >= 8:
                self.ledIndex = 0

    def show2(self):
        if time.time() > (self.startTime + self.interval):
            self.startTime = time.time()
            self.resetStrip()
            self.strip.setPixelColorRGB(self.ledIndex, 20, 0, 0)
            self.strip.setPixelColorRGB((self.ledIndex + self.prevLed), 5, 0, 0)
            self.strip.show()

            self.ledIndex += self.step

            if self.ledIndex >= 7:
                self.step = -1
                self.prevLed = 1

            if self.ledIndex <= 0:
                self.step = 1
                self.prevLed = -1
        
    def run(self):
        while True:
            if self.currentShow == 'show1':
                self.show1()
            elif self.currentShow == 'show2':
                self.show2()
            else:
                self.idle()
        

if __name__ == '__main__':
    lsa = LightShowApp()
    lsa.run()
    