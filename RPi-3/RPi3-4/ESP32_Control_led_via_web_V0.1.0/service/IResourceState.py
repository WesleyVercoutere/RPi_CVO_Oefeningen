from domain.RequestObject import RequestObject
from service.LedService import LedService

class IResourceState:

    def __init__(self, led_service: LedService) -> None:
        self._led_service = led_service

    def get_content(self, request_obj: RequestObject):
        raise NotImplementedError

    def get_header(self):
        raise NotImplementedError
