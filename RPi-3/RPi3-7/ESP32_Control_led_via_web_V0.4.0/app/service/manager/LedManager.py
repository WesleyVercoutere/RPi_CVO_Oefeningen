from machine import Pin

from app.domain.Led import Led
from app.service.mapper.LedMapper import LedMapper


class LedManager:

    def __init__(self, led_mapper: LedMapper) -> None:
        self._mapper = led_mapper
        self._repo =
        

    def get_all_leds(self):
        pass

    def led_on(self):
        self.led.state = True

    def led_off(self):
        self.led.state = False

    def led_toggle(self):
        self.led.state = not self.led.state

    def get_led(self):
        return self._mapper.map_to_dto(self.led)
    