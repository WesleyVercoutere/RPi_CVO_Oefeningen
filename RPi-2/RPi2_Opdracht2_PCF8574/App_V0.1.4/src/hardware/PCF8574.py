import RPi.CPIO as GPIO
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
        self.reset()

    def _setup(self):
        GPIO.setup(self._interruptPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._interruptPin.setEvent(edge=GPIO.FALLING, callback=lambda x: self._processInputs(), bouncetime=0)

    def _processInputs(self):
        print("Do stuff")

    def _readI2C(self):
        self._message = self.bus.read_byte(self._address)

    def _writeI2C(self):
        self.bus.write_byte(self._address, self._message)

    def _setBit(self, value, bit):
        return value | (1 << bit)

    def _clearBit(self, value, bit):
        return value & ~(1 << bit)

    def _isSet(self, value, bit):
        return value & 1 << bit != 0

    def addInput(self, *args):
        for i in args:
            print(i)

    def addOutput(self, *args):
        for i in args:
            print(i)

    def reset(self):
        self._message = 255
        self.bus.write_byte(self._address, self._message)
