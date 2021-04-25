import smbus


class PCF8574:

    def __init__(self, address):
        self.bus = smbus.SMBus(1)

        self._address = address
        self._message = 0

        self.reset()

    def reset(self):
        self._message = 0
        self.bus.write_byte(self._address, self._message)

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
