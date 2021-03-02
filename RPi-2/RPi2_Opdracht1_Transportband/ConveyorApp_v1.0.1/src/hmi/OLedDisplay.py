from service.observer.Observer import Observer


class OLedDisplay(Observer):

    def __init__(self, display, conveyorManager):
        self.display = display

        conveyorManager.addObserver(self)

    def update(self, *args, **kwargs):
        pass

    def loop(self):
        pass


"""

from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

from PIL import Image, ImageDraw

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)



# serial_i2c = i2c(port=1, address=0x3C)
# serial_spi = spi(device=0, port=0)

# substitute ssd1331(...) or sh1106(...) below if using that device
device_i2c = sh1106(i2c(port=1, address=0x3C), rotate=0)
# device_spi = ssd1306(serial_spi)

# with is een contextmanager die __enter__() en __exit__() methodes aanroept bi jstart en einde 

# with canvas(device_spi) as draw:
#     draw.rectangle(device_spi.bounding_box, outline="white", fill="black")
#     draw.text((10, 40), ">Hello World SPI", fill="white")

dither = False
image = Image.new("RGB" if dither else device_i2c.mode, device_i2c.size)
draw = ImageDraw.Draw(image)

draw.text((10, 40), ">Hello World I2C", fill="white")
draw.text((10, 10), ">Hello World I2C", fill="white")
print(draw.__sizeof__())

device_i2c.display(image)

time.sleep(2)

draw.rectangle(device_i2c.bounding_box, outline="black", fill="black")
draw.text((10, 40), "Wesley", fill="white")
print(draw.__sizeof__())


device_i2c.display(image)

time.sleep(2)


# draw.text((10, 40), ">Hello World I2C", fill="white")

# device_i2c.display(image)

# time.sleep(5)
# print("show rectangle")

# draw.rectangle(device_i2c.bounding_box, outline="white", fill="black")
# device_i2c.display(image)

# time.sleep(5)
# print("show text + rectangle")


# draw.rectangle(device_i2c.bounding_box, outline="white", fill="black")
# draw.text((10, 40), ">Hello World I2C", fill="white")
# device_i2c.display(image)

# time.sleep(5)

# device_i2c.clear()

# draw.text((10, 40), ">Hello World I2C", fill="white")

# device_i2c.display(image)

# time.sleep(5)

# draw.text((10, 10), ">Hello World hoger", fill="white")

# device_i2c.display(image)




# draw.rectangle(device_i2c.bounding_box, outline="white", fill="black")

# with canvas(device_i2c) as draw:
#     draw.rectangle(device_i2c.bounding_box, outline="white", fill="black")
#     draw.text((10, 40), ">Hello World I2C", fill="white")





while True:
    pass

"""