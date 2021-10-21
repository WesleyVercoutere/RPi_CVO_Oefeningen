import json

from app.service.manager.LedManager import LedManager
from webserver.WebServer import WebServer


class Controller:

    def __init__(self, web_server: WebServer, led_manager: LedManager) -> None:
        self._web = web_server
        self._led_mgr = led_manager

    def register_routes(self):

        @self._web.register_route_html("/", "/home", "/index")
        def get_home_page():
            self._led_mgr.led_off()

            return "resources/html/index.html"

        @self._web.register_route_api("/led_on")
        def set_led_on():
            self._led_mgr.led_on()

        @self._web.register_route_api("/led_off")
        def set_led_off():
            self._led_mgr.led_off()

        @self._web.register_route_api("/toggle")
        def toggle_led():
            self._led_mgr.led_toggle()

        @self._web.register_route_api("/get_led_info")
        def get_led_info():
            return json.dumps(self._led_mgr.get_led().__dict__)
