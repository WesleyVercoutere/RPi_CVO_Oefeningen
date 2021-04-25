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
        self.reset()

    def _setup(self):
        GPIO.setup(self._interruptPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self._interruptPin, edge=GPIO.FALLING, callback=lambda x: self._processInputs())

    def _processInputs(self):
        self._readI2C()
        
        for i in self._inputs:
            if self._isSet(i.getPin()):
                i.callEvent()

    def _readI2C(self):
        self._message = self.bus.read_byte(self._address)

    def _writeI2C(self):
        self.bus.write_byte(self._address, self._message)

    def _setBit(self, bit):
        self._message =  self._message | (1 << bit)

    def _clearBit(self, bit):
        self._message =  self._message & ~(1 << bit)

    def _isSet(self, bit):
        return self._message & 1 << bit != 0

    def addInput(self, *args):
        for input in args:
            # eventueel controleren of object in args een type is van DigitalInputPCF8574
            self._inputs.append(input)

    def addOutput(self, *args):
        for i in args:
            # eventueel controleren of object in args een type is van DigitalOutputPCF8574
            self._outputs.append(i)
            i.setPCF8574(self)

    def reset(self):
        self._message = 255
        self.bus.write_byte(self._address, self._message)

    def updateOutput(self, output):
        if output.getState:
            self._clearBit(output.getPin())
        else:
            self._setBit(output.getPin())

        self._writeI2C()
