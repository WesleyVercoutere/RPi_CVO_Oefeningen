from service.IResourceState import IResourceState
from domain.RequestObject import RequestObject
from service.LedService import LedService

class HTMLState(IResourceState):

    def __init__(self, led_service: LedService) -> None:
        super().__init__(led_service)

    def get_content(self, request_obj: RequestObject):
        file =  f"/resources/{request_obj.filename}"
        file = open(file, "r")

        content = file.read()

        if "led_on" in request_obj.filename:
            self._led_service.led_on()

        if "led_off" in request_obj.filename:
            self._led_service.led_off()

        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/html\r\n"

