from machine import Pin

from app.domain.Led import Led
from app.service.mapper.LedMapper import LedMapper


class LedManager:

    def __init__(self, led_mapper: LedMapper) -> None:
        self._mapper = led_mapper

        self.ledOnBoard = Pin(14, Pin.OUT)
        self.led = Led(pin_nr=14, color="red")
        self.led_off()

    def led_on(self):
        print("led on")
        self.led.state = True
        self.ledOnBoard.on()

    def led_off(self):
        print("led off")
        self.led.state = False
        self.ledOnBoard.off()

    def led_toggle(self):
        print("led toggle")
        self.led.state = not self.led.state
        self.ledOnBoard.value(not self.ledOnBoard.value())

    def get_led(self):
        return self._mapper.map_to_dto(self.led)
    