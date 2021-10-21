import time
from machine import Pin

from app.service.manager.ButtonManager import ButtonManager
from app.service.manager.LedManager import LedManager


class HardwareManager:

    def __init__(self, led_service: LedManager, btn_service: ButtonManager) -> None:
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
