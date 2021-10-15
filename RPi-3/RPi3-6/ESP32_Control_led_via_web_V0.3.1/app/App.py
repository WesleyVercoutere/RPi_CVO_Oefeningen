from threading import Thread

from app.controller.Controller import Controller
from app.service.ButtonService import ButtonService
from app.service.HardwareService import HardwareService
from app.service.LedService import LedService
from webserver.WebServer import WebServer


class App:

    def __init__(self) -> None:
        self._led_service = LedService()
        self._btn_service = ButtonService()
        self._hw_service = HardwareService(self._led_service, self._btn_service)

        self._init_hardware()

        self._web_server = WebServer()
        self._controller = Controller(self._web_server, self._led_service)

    def run(self) -> None:
        self._controller.register_routes()

        t1 = Thread(target=self._hw_service.run)
        t2 = Thread(target=self._web_server.run)

        t1.start()
        t2.start()

    def _init_hardware(self):
        print("init buttons and leds, add them to the repos and services...")
