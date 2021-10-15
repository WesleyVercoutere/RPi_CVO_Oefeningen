import time

from app.service.ButtonService import ButtonService
from app.service.LedService import LedService


class HardwareService:

    def __init__(self, led_service: LedService, btn_service: ButtonService) -> None:
        self._led_service = led_service
        self._btn_service = btn_service

        self._counter = 0
        self._start_time = time.time()

    def run(self) -> None:
        while True:
            if self._update():
                self._counter += 1
                print(f"HW service counter = {self._counter}")

    def _update(self) -> bool:
        current_time = time.time()

        if current_time >= self._start_time + 1:
            self._start_time = current_time
            return True

        return False
