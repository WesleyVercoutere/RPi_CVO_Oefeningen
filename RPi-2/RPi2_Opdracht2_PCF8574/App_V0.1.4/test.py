import RPi.GPIO as GPIO
import smbus

class PCF8574:

    def __init__(self, address, interruptPin):
        self.bus = smbus.SMBus(1)

        self._inputs = []
        self._outputs = []

        self._interruptPin = interruptPin
        self._address = address
        self._message = 0

        self._setup()
        # self.reset()

    def _setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._interruptPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._interruptPin, edge=GPIO.FALLING, callback=lambda x: self._processInputs())

    def _processInputs(self):
        print("Do stuff")

if __name__ == "__main__":
    pcf = PCF8574(0x20, 18)

    while True:
        pass