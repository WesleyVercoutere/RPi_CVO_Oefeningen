import time
from app.domain.Button import Button
from app.domain.Led import Led
from machine import Pin

from app.service.manager.ButtonManager import ButtonManager
from app.service.manager.LedManager import LedManager


class HardwareManager:

    def __init__(self, led_mgr: LedManager, btn_mgr: ButtonManager) -> None:
        self._led_mgr = led_mgr
        self._btn_mgr = btn_mgr

        self._init_hardware()

    def set_callbacks(self):
        leds = self._led_mgr.get_all_leds()
        btns = self._btn_mgr.get_all_buttons()

        for i in range(len(btns)):
            self._set_callback(btns[i], leds[i])
    
    def run(self) -> None:
        while True:
            pass

    def _init_hardware(self) -> None:
        self._init_leds()
        self._init_buttons()

    def _init_leds(self) -> None:
        led_1 = Led(pin_nr=13, color="Red")
        led_2 = Led(pin_nr=12, color="Green")
        led_3 = Led(pin_nr=14, color="Blue")
        led_4 = Led(pin_nr=27, color="Yellow")

        self._led_mgr.add_leds(led_1, led_2, led_3, led_4)

    def _init_buttons(self) -> None:
        btn_1 = Button(pin_nr=5)
        btn_2 = Button(pin_nr=18)
        btn_3 = Button(pin_nr=19)
        btn_4 = Button(pin_nr=21)

        self._btn_mgr.add_buttons(btn_1, btn_2, btn_3, btn_4)

    def _set_callback(self, btn, led):
        btn.get_pin().irq(trigger=Pin.IRQ_FALLING, handler=lambda _:self._callback_toggle_led(led))

    def _callback_toggle_led(self, led):
        self._led_mgr.led_toggle(led)
        time.sleep(0.1)
