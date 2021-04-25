import smbus


class DigitalOutputPCF8574:

    def __init__(self, port):
        self._port = port
        self._pcfAddress = 0x20
        self._pcfMessage = 0
        self._bus = smbus.SMBus(1)

    def _readI2C(self):
        self._pcfMessage = self._bus.read_byte(self._pcfAddress)

    def _writeI2C(self):
        self._bus.write_byte(self._pcfAddress, self._pcfMessage)

    def _setBit(self, value, bit):
        return value | (1 << bit)

    def _clearBit(self, value, bit):
        return value & ~(1 << bit)

    def _isSet(self, value, bit):
        return value & 1 << bit != 0

    def toggle(self):
        self._readI2C()

        statusLed = self._isSet(self._pcfMessage, self._port)

        if statusLed:
            self._pcfMessage = self._clearBit(self._pcfMessage, self._port)
        else:
            self._pcfMessage = self._setBit(self._pcfMessage, self._port)

        self._writeI2C()
