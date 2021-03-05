from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

from PIL import Image, ImageDraw

from service.observer.Observer import Observer


class OLedDisplay(Observer):

    def __init__(self, conveyorManager):
        self.display = display

        serial_i2c = i2c(port=1, address=0x3C)
        self.display = sh1106(serial_i2c, rotate=0)

        self.startUpMessage()

        conveyorManager.addObserver(self)

    def startUpMessage(self):
        with canvas(self.display) as draw:
            draw.text((0, 0), "Starting conveyor...", fill="white")

    def updateDisplay(self, message):
        with canvas(self.display) as draw:
            # draw.rectangle(self.display.bounding_box, outline="white", fill="black")
            draw.text((1, 1), message, fill="white")

    def update(self, *args, **kwargs):
        message = kwargs["message"]
        self.updateDisplay(message)
