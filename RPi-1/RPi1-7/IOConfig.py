try:
    import RPi.GPIO as GPIO
except:
    from dummygpio.DummyGPIO import DummyGPIO
    GPIO = DummyGPIO(True)

class IOConfig:

    def __init__(self):
        pass

