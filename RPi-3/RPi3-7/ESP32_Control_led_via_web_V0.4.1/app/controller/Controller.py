import json

from app.service.manager.LedManager import LedManager
from webserver.WebServer import WebServer
from webserver.util.HTTPRequestMethod import HTTPRequestMethod
from webserver.util.RequestType import RequestType


class Controller:

    def __init__(self, web_server: WebServer, led_manager: LedManager) -> None:
        self._web = web_server
        self._led_mgr = led_manager

    def register_routes(self):

        @self._web.register_route("/", "/home", "/index")
        def get_home_page():
            return "resources/html/index.html"

        @self._web.register_route("/led_on/{id}", type=RequestType.REST, method=HTTPRequestMethod.GET)
        def set_led_on(id):
            self._led_mgr.led_on(id)

        @self._web.register_route("/led_off/{id}", type=RequestType.REST, method=HTTPRequestMethod.GET)
        def set_led_off(id):
            self._led_mgr.led_off(id)

        # @self._web.register_route_api("/toggle")
        # def toggle_led():
        #     self._led_mgr.led_toggle()

        @self._web.register_route("/get_led_info", type=RequestType.REST, method=HTTPRequestMethod.GET)
        def get_led_info():
            leds = self._led_mgr.get_all_led_dtos()
            return json.dumps([led.__dict__ for led in leds])
