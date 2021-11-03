from machine import Pin

from app.domain.Led import Led
from app.repository.LedRepository import LedRepository
from app.service.mapper.LedMapper import LedMapper


class LedManager:

    def __init__(self, led_mapper: LedMapper, led_repo: LedRepository) -> None:
        self._mapper = led_mapper
        self._repo = led_repo

    def add_leds(self, *leds):
        [self._repo.create(led) for led in leds]

    def get_all_leds(self):
        return self._repo.read_all()

    def get_all_led_dtos(self):
        dtos = list()

        for led in self._repo.read_all():
            dto = self._mapper.map_to_dto(led)
            dtos.append(dto)

        return dtos

    def led_on(self, id):
        led: Led = self._repo.read_by_id(id)
        led.state = True
        led.get_pin().on()

    def led_off(self, id):
        led: Led = self._repo.read_by_id(id)
        led.state = False
        led.get_pin().off()

    def led_toggle(self, led: Led):
        led.state = not led.state
        led.get_pin().value(led.state)

    def get_led(self):
        return self._mapper.map_to_dto(self.led)
