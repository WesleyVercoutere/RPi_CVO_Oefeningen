import time
from machine import Pin

from app.service.ButtonService import ButtonService
from app.service.LedService import LedService


class HardwareService:

    def __init__(self, led_service: LedService, btn_service: ButtonService) -> None:
        self._led_service = led_service
        self._btn_service = btn_service

    def set_callbacks(self):
        self._btn_service.btn_1.irq(trigger=Pin.IRQ_FALLING, handler=self._callback_toggle_led)

    def run(self) -> None:
        while True:
            pass

    def _callback_toggle_led(self, pin):
        self._led_service.led_toggle()
        time.sleep(0.1)
