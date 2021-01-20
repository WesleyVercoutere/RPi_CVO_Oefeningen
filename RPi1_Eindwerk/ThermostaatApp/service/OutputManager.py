import RPi.GPIO as GPIO
from rpi_ws281x import *

class OutputManager:

    def __init__(self):
        self.init()

    def init(self):
        self.initLedStrip()

    def initLedStrip(self):
        # LED strip configuration:
        LED_COUNT      = 8      # Number of LED pixels.
        LED_PIN        = 13  # GPIO pin connected to the pixels (18 uses PWM!).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10     # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 1       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()
        self.resetStrip()

    def resetStrip(self):
        for i in range(8):
            self.strip.setPixelColorRGB(i, 0, 0, 0)
  
        self.strip.show()

    def toggleLed(self, status):
        brightness = 0

        if status:
            brightness = 100

        for i in range(8):
            self.strip.setPixelColorRGB(i, brightness, brightness, brightness)
        
        self.strip.show()
