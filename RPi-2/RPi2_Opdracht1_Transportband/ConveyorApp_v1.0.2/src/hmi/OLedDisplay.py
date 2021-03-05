from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, sh1106

from service.observer.Observer import Observer


class OLedDisplay(Observer):

    def __init__(self, oLedDisplayManager, conveyorManager):
        self.mgr = oLedDisplayManager

        serial_i2c = i2c(port=1, address=0x3C)
        self.display = sh1106(serial_i2c, rotate=0)

        self.startUpMessage()

        conveyorManager.addObserver(self)

    def startUpMessage(self):
        with canvas(self.display) as draw:
            draw.text((0, 0), "Starting conveyor...", fill="white")

    def updateDisplay(self, message):
        dto = self.mgr.getDisplayDTO()

        with canvas(self.display) as draw:
            # draw.rectangle(self.display.bounding_box, outline="white", fill="black")
            draw.text((1, 1), message, fill="white")

    def update(self, *args, **kwargs):
        message = kwargs["message"]
        self.updateDisplay(message)
