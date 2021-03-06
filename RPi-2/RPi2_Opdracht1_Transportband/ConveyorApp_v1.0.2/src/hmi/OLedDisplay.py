from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

from util.observer import Observer


class OLedDisplay(Observer):

    def __init__(self, oLedDisplayManager, conveyorManager):
        self.display = None
        self.setupDisplay()

        self.startUpMessage()

        self.mgr = oLedDisplayManager
        self.conveyorMgr = conveyorManager
        self.conveyorMgr.addObserver(self)

    def setupDisplay(self):
        serial_i2c = i2c(port=1, address=0x3C)
        self.display = sh1106(serial_i2c, rotate=0)

    def startUpMessage(self):
        with canvas(self.display) as draw:
            draw.text((15, 5), "Starting conveyor...", fill="white")

    def updateDisplay(self, message):
        dto = self.mgr.getDisplayDTO(self.conveyorMgr.conveyor)

        with canvas(self.display) as draw:
            draw.text((2, 5), dto.state, fill="white")
            draw.text((50, 5), dto.position, fill="white")
            draw.text((100, 5), dto.nbrOfSteps, fill="white")

            draw.text((2, 25), message, fill="white")

    def update(self, *args, **kwargs):
        message = kwargs["message"]
        self.updateDisplay(message)
