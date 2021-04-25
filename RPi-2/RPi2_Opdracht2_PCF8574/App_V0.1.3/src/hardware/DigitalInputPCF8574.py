import RPi.GPIO as GPIO
import smbus


class DigitalInputPCF8574:

    def __init__(self, port):
        self._port = port
        self._pcfAddress = 0x20
        self._pcfMessage = 0
        self._bus = smbus.SMBus(1)

        self._callback = None

        # Dit kan niet!!
        # GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.add_event_detect(18, edge=GPIO.FALLING, callback=lambda _: self.runCallback())

    def _readI2C(self):
        self._pcfMessage = self._bus.read_byte(self._pcfAddress)

    def _isSet(self, value, bit):
        return value & 1 << bit != 0

    def runCallback(self):
        self._readI2C()

        if self._isSet(self._pcfAddress, self._port):
            self._callback()

    def setEvent(self, callback):
        self._callback = callback
