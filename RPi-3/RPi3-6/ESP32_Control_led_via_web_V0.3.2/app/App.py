from app.controller.Controller import Controller
from app.service.manager.ButtonManager import ButtonManager
from app.service.manager.HardwareManager import HardwareManager
from app.service.manager.LedManager import LedManager
from webserver.WebServer import WebServer


class App:

    def __init__(self) -> None:
        self._led_mgr = LedManager()
        self._btn_mgr = ButtonManager()
        self._hw_mgr = HardwareManager(self._led_mgr, self._btn_mgr)
        self._web_server = WebServer()
        self._controller = Controller(self._web_server, self._led_mgr)

    def run(self) -> None:
        self._controller.register_routes()
        self._hw_mgr.set_callbacks()
        self._web_server.run()

        # _thread.start_new_thread(self._hw_service.run, ())
        # _thread.start_new_thread(self._web_server.run, ())
